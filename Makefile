BOOTSTRAP = ./stylesheets/css/bootstrap.css
BOOTSTRAP_LESS = ./stylesheets/less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ./stylesheets/css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ./stylesheets/less/responsive.less
LESS_COMPRESSOR ?= `which lessc`

bootstrap:
	lessc ${BOOTSTRAP_LESS} > stylesheets/css/bootstrap.css
	lessc --compress ${BOOTSTRAP_LESS} > stylesheets/css/bootstrap.min.css
	lessc ${BOOTSTRAP_RESPONSIVE_LESS} > stylesheets/css/bootstrap-responsive.css
	lessc --compress ${BOOTSTRAP_RESPONSIVE_LESS} > stylesheets/css/bootstrap-responsive.min.css
	cat stylesheets/nonfinal-js/bootstrap-transition.js stylesheets/nonfinal-js/bootstrap-alert.js stylesheets/nonfinal-js/bootstrap-button.js stylesheets/nonfinal-js/bootstrap-carousel.js stylesheets/nonfinal-js/bootstrap-collapse.js stylesheets/nonfinal-js/bootstrap-dropdown.js stylesheets/nonfinal-js/bootstrap-modal.js stylesheets/nonfinal-js/bootstrap-tooltip.js stylesheets/nonfinal-js/bootstrap-popover.js stylesheets/nonfinal-js/bootstrap-scrollspy.js stylesheets/nonfinal-js/bootstrap-tab.js stylesheets/nonfinal-js/bootstrap-typeahead.js > stylesheets/js/bootstrap.js	
	uglifyjs -nc stylesheets/js/bootstrap.js > stylesheets/js/bootstrap.min.js

