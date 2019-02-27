$(document).ready(function() {
  serverlessURL = 'https://us-central1-neuronio-edp.cloudfunctions.net/teste-03';

  var canvas = document.createElement('canvas');
  canvas.width = 96;
  canvas.height = 96;
  var ctx = canvas.getContext("2d");

  // [
  //   '10037', '11640', '14739', '15913', '21253', '22383', '23516', '2958',
  //   '31562', '6827', '10978', '11646', '15184', '19625', '22285', '23472',
  //   '28947', '30915', '4693', '7974'
  // ].forEach(addCard);
  [
    '10037',
  ].forEach(addCard);

  function addCard(cell, index, array) {
    $('body').append(
      `
      <div class="card" id="${cell}">
        <img src="cells/${cell}.png" style="width:100%; height: 300px;">
        <div class="container">
          <h4><b>ID: </b>${cell}</h4>
        </div>
        <div class="result">WAITING FOR RESULT</div>
      </div>
      `
    );
    var img = $(`#${cell}`).children()[0];

    const toDataURL = url => fetch(url)
    .then(response => response.blob())
    .then(blob => new Promise((resolve, reject) => {
      const reader = new FileReader()
      reader.onloadend = () => resolve(reader.result)
      reader.onerror = reject
      reader.readAsDataURL(blob)
    }))

    toDataURL(img.src)
    .then(dataUrl => {
      console.log('RESULT:', dataUrl)
    })

    // img.onload = function() {
    //   ctx.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight, 0, 0, 96, 96);
    //   imageData = ctx.getImageData(0, 0, 224, 224);
    //   var dataURL = canvas.toDataURL();
    //   // dataURL = dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
    //   // dataURL = dataURL + "=".repeat((4 - (dataURL.length % 4)) % 4);
    //   console.log(dataURL)
    //   axios({
    //     method: 'post',
    //     url: serverlessURL,
    //     data: Qs.stringify({
    //       image_base64: dataURL
    //     }),
    //     headers: {
    //       'Accept': 'application/x-www-form-urlencoded',
    //       'Content-Type': 'application/x-www-form-urlencoded'
    //     }
    //   }).then(function(response) {
    //     console.log(`${cell} - ${response}`);
    //   });
    // }
  };
});
