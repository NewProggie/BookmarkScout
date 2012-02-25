DIRNAME = content
BOOTSTRAP = ./${DIRNAME}/css/bootstrap.css
BOOTSTRAP_LESS = ./${DIRNAME}/less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ./${DIRNAME}/css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ./${DIRNAME}/less/responsive.less
BS_NFJS = ${DIRNAME}/nonfinal-js/bootstrap
LESS_COMPRESSOR ?= `which lessc`

bootstrap:
	lessc ${BOOTSTRAP_LESS} > ${DIRNAME}/css/bootstrap.css
	lessc --compress ${BOOTSTRAP_LESS} > ${DIRNAME}/css/bootstrap.min.css
	lessc ${BOOTSTRAP_RESPONSIVE_LESS} > ${DIRNAME}/css/bootstrap-responsive.css
	lessc --compress ${BOOTSTRAP_RESPONSIVE_LESS} > ${DIRNAME}/css/bootstrap-responsive.min.css
	cat ${BS_NFJS}-transition.js ${BS_NFJS}-alert.js ${BS_NFJS}-button.js ${BS_NFJS}-carousel.js ${BS_NFJS}-collapse.js ${BS_NFJS}-dropdown.js ${BS_NFJS}-modal.js ${BS_NFJS}-tooltip.js ${BS_NFJS}-popover.js ${BS_NFJS}-scrollspy.js ${BS_NFJS}-tab.js ${BS_NFJS}-typeahead.js > ${DIRNAME}/js/bootstrap.js
	uglifyjs -nc ${DIRNAME}/js/bootstrap.js > ${DIRNAME}/js/bootstrap.min.js
