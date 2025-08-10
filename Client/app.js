function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url =  "/api/predict_home_price";
;

  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function (data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    console.log(status);
  });
}

function onPageLoad() {
    console.log("document loaded");
    var url = "/api/get_location_names";

    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");

        if (data && data.locations) {
            var locations = data.locations;

            $('#uiLocations').empty();
            $('#uiLocations')
              .append(new Option('Choose a Location', '', true, true))
              .prop('disabled', false);

            for (var i in locations) {
                console.log("Adding:", locations[i]); 
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}


window.onload = onPageLoad;
