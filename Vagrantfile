# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise64"

  config.vm.network "forwarded_port", guest: 80, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    echo "Updating sources..."
    sed -i 's/us.archive/uk.archive/g' /etc/apt/sources.list
    sudo apt-get update -y

    echo "Installing packages..."
    sudo apt-get install -y make python-dev libpcre3-dev nginx python-pip libmysqlclient-dev libldap2-dev libsasl2-dev libxml2-dev libxslt1-dev

    echo "Updating python requirements..."
    sudo pip install -r /vagrant/requirements.txt

    echo "Configuring uwsgi and nginx"
    sudo mkdir /etc/uwsgi
    sudo ln -s /vagrant/conf/develop/uwsgi/stock.ini /etc/uwsgi/stock.ini
    sudo sed -i '/exit 0/i \/usr\/local\/bin\/uwsgi --emperor \/etc\/uwsgi --daemonize \/var\/log\/uwsgi.log' /etc/rc.local
    sudo /usr/local/bin/uwsgi --emperor /etc/uwsgi --daemonize /var/log/uwsgi.log
    sudo ln -s /vagrant/conf/develop/nginx/stock.conf /etc/nginx/sites-enabled/stock.conf
    sudo rm /etc/nginx/sites-enabled/default
    
    cd /vagrant/stock_management/
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --noinput
    
    export DJANGO_SETTINGS_MODULE="stock_management.settings"
    python -c 'from django.contrib.auth.models import User; User.objects.create_superuser("admin", "admin@admin.com", "stock")'
    
    echo "########################################################"
    echo "Stock now serving on host machine: 127.0.0.1:8000"
    echo "########################################################"
  SHELL
  
  config.vm.provision "shell", inline: "sudo /etc/init.d/nginx restart", run: "always"

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
end
