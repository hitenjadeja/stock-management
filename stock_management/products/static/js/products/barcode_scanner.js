$(function() {
    Quagga.init({
        inputStream : {
          name : "Live",
          type : "LiveStream"
        },
        decoder : {
          readers : ["ean_reader", "ean_8_reader"]
        }
      }, function(err) {
          if (err) {
              console.log(err);
              return
          }
          console.log("Initialization finished. Ready to start");
          Quagga.start();
      });

    Quagga.onDetected(function(result) {
        var code = result.codeResult.code;
        $('#id_barcode').val(code);
        console.log(code);
        Quagga.stop();
    });
});