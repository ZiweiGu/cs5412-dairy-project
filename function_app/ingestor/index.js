module.exports = function (context, IoTHubMessages) {
    context.log(`JavaScript eventhub trigger function called for message array: ${IoTHubMessages}`);

    var farmID = "";
    var reg = "";
    var dateTime = new Date();
    var lie = 0;
    var stand = 0;
    var walk = 0;
    var runminate = 0;
    var nothing = 0;
    var inactive = 56;
    var active = 4;
    var highActive = 0;

    var deviceId = "";

    IoTHubMessages.forEach(message => {
        context.log(`Processed message: ${JSON.stringify(message)}`);
        farmID = message["Farm ID"];
        reg = message["Reg"];
        lie = message["lie"];
        stand = message["stand"];
        walk = message["walk"];
        runminate = message["ruminate"];
        nothing = message["nothing"];
        inactive = message["inactive"];
        active = message["active"];
        highActive = message["highActive"];
    });

    var output = {
        "datetime": dateTime,
        "farmID": farmID,
        "reg": reg,
        "lie": parseInt(lie),
        "stand": parseInt(stand),
        "walk": parseInt(walk),
        "ruminate": parseInt(runminate),
        "nothing": parseInt(nothing),
        "inactive": parseInt(inactive),
        "active": parseInt(active),
        "highActive": parseInt(highActive)
    };

    context.log(`Output content: ${JSON.stringify(output)}`);

    context.bindings.outputDocument = output;

    context.done();
};