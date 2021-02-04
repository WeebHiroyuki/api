var appRouter = function (app) {
    const { parse } = require("@devsnowflake/text-emoji-parser");
    const { EmojiAPI } = require("emoji-api");
    const Client = new EmojiAPI();

    // homepage
    app.get("/", function(req, res) {
      res.status(200).send('girl idk how to do frontend');
    } )

    // all emoji endpoint
    app.get("/emoji/image/all/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    res.json({url: emoji.images }) })} )

    // apple image endpoint
    app.get("/emoji/image/apple/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Apple) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Apple.url } ) } ) } )

    // google image endpoint
    app.get("/emoji/image/google/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
      if (!emoji.Google) return res.status(404).send("they don't have that")
      res.json({ url: emoji.Google.url } ) } ) } )

    // samsung image endpoint
    app.get("/emoji/image/samsung/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
      if (!emoji.Samsung) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Samsung.url } ) } ) } )    

    // microsoft image endpoint
    app.get("/emoji/image/microsoft/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Microsoft) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Microsoft.url } ) } ) } )

    // whatsapp image endpoint
    app.get("/emoji/image/whatsapp/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.WhatsApp) return res.status(404).send("they don't have that")
    res.json({ url: emoji.WhatsApp.url } ) } ) } )
  
    // twitter image endpoint
    app.get("/emoji/image/twitter/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Twitter) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Twitter.url } ) } ) } )

    // facebook image endpoint
    app.get("/emoji/image/facebook/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Facebook) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Facebook.url } ) } ) } )    

    // joypixels image endpoint
    app.get("/emoji/image/joypixels/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.JoyPixels) return res.status(404).send("they don't have that")
    res.json({ url: emoji.JoyPixels.url } ) } )} )

    // openmoji image endpoint
    app.get("/emoji/image/openmoji/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.OpenMoji) return res.status(404).send("they don't have that")
    res.json({ url: emoji.OpenMoji.url } ) } ) } )

    // emojidex image endpoint
    app.get("/emoji/image/emojidex/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    console.log(emoji.images)
    res.json({ url: emoji.Emojidex.url } ) } ) } )

    // facebook messenger image endpoint
    app.get("/emoji/image/messenger/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Messenger) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Messenger.url } ) } ) } )    

    // lg image endpoint
    app.get("/emoji/image/lg/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.LG) return res.status(404).send("they don't have that")
    res.json({ url: emoji.LG.url } ) } ) } )
    
    // htc image endpoint
    app.get("/emoji/image/htc/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.HTC) return res.status(404).send("they don't have that")
    res.json({ url: emoji.HTC.url } ) } ) } )

    // mozilla image endpoint
    app.get("/emoji/image/mozilla/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
      if (!emoji.Mozilla) return res.status(404).send("they don't have that")
      res.json({ url: emoji.Mozilla.url } ) } ) } )

    // softbank image endpoint
    app.get("/emoji/image/softbank/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.SoftBank) return res.status(404).send("they don't have that")
    res.json({ url: emoji.SoftBank.url } ) } ) } )     
      
    // docomo image endpoint
    app.get("/emoji/image/docomo/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    if (!emoji.Docomo) return res.status(404).send("they don't have that")
    res.json({ url: emoji.Docomo.url } ) } ) } )

    // emoji name endpoint
    app.get("/emoji/name/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    res.json({ name: emoji.name }) })} )

    // emoji description endpoint
    app.get("/emoji/description/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    res.json({ description: emoji.description }) })} )

    // emoji unicode endpoint
    app.get("/emoji/unicode/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    res.json({ unicode: emoji.unicode }) })} )

    // emoji shortcodes endpoint
    app.get("/emoji/shortcodes/:emoji/", function(req, res) {
    var message = req.params.emoji;
    const message_parsed = parse(message)
    if (!message_parsed.length) return res.status(404).send('bestie where is the emoji');
    const emoji = message_parsed[0]
    Client.get(emoji.text)
    .then(emoji => {
    res.json({ shortcodes: emoji.shortCodes }) })} )





    // basically 404 route
    app.get('*', function(req, res){
      res.status(404).send('nothing is here, go away');
    });

}

module.exports = appRouter;