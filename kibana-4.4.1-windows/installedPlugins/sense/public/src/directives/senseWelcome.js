require('./senseHelpExample');

const storage = require('../storage');

require('ui/modules')
.get('app/sense')
.directive('senseWelcome', function () {
  return {
    restrict: 'E',
    template: require('./welcome.html'),
    link: function ($scope) {
      // date junk is a work around for https://github.com/elastic/kibana/pull/5167
      var shown = Date.now();

      $scope.$on('$destroy', function () {
        if (Date.now() - shown > 1000) {
          storage.set('version_welcome_shown', '1c4b1e7e31a50121a423d2c648bc4434a722002e');
        }
      });
    }
  }
});
