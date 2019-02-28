$(document).ready(function() {
  serverlessURL = 'your-function-url-goes-here';

  const toDataURL = url => fetch(url).then(
    response => response.blob()).then(
    blob => new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(blob)
    }));

  [
    '10037', '11640', '14739', '15913', '21253', '22383', '23516', '2958',
    '31562', '6827', '10978', '11646', '15184', '19625', '22285', '23472',
    '28947', '30915', '4693', '7974'
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

    toDataURL(`https://github.com/adrianodennanni/serverless_deep_learning_deploy_example/raw/master/example_web_page/cells/${cell}.png`)
      .then(dataUrl => {
        axios({
          method: 'post',
          url: serverlessURL,
          data: Qs.stringify({
            image_base64: dataUrl.replace(/^data:image\/(png|jpg);base64,/, "")
          }),
          headers: {
            'Accept': 'application/x-www-form-urlencoded',
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(function(response) {
          var data = JSON.parse(response.data.replace(/'/g,"\""));
          var parasitized = data['Parasitized'];
          var uninfected = data['Uninfected'];
          console.log()
          if (parasitized > uninfected) {
            $(`#${cell} div.result`).css("background-color", "red");
            $(`#${cell} div.result`).text('Parasitized');
          } else {
            $(`#${cell} div.result`).css("background-color", "green");
            $(`#${cell} div.result`).text('Uninfected');
          }
        });
      });
  };
});
