
/*
 * GET home page.
 */

var mongoose = require('mongoose')
    , Name = mongoose.model('Name');

exports.index = function(req, res){
    Name.findOne().exec(function(err, user){
        console.log(user);
        res.render('index', { title: 'Express' });
    });
};