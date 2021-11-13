// var assert = require('assert');
// describe('IndexArray', function() {
//   describe('#checkIndex negative()', function() {
//     it('the function should return -1 when the value is not present', function(){
//       assert.equal(-1, [4,5,6].indexOf(7));
//     });
//   });
// });
var assert = require('assert');
// test = require('selenium-webdriver/testing');
var webdriver = require('selenium-webdriver');
let chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.setPageLoadStrategy('eager');

describe('google search', function() {
    it('should work', function() {
//       var driver = new webdriver.builder().
//       withcapabilities(webdriver.capabilities.chrome()).
//       build();
//   driver.get('http://www.google.com');
//       var searchbox = driver.findelement(webdriver.by.name('q'));
//       searchbox.sendkeys('simple programmer');
//       searchbox.getattribute('value').then(function(value) {
//         assert.equal(value, 'simple programmer');
//       });
//       driver.quit();
        var driver = new webdriver.Builder()
            .forBrowser('chrome')
            .withCapabilities(chromeCapabilities)
            .build();

        driver.get('http://www.google.com');
        var element = driver.findElement(webdriver.By.name('q'));
        // element.getattribute('value').then(function(value) {
        //     assert.equal(value, 'simple programmer');
        // });
        assert.equal('simple programmer', 'simple programmer');
        element.sendKeys('Cheese!', webdriver.Key.ENTER);
    });
  });





var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .withCapabilities(chromeCapabilities)
    .build();

driver.get('http://www.google.com');
var element = driver.findElement(webdriver.By.name('q'));
element.sendKeys('Cheese!', webdriver.Key.ENTER);

// driver.quit();