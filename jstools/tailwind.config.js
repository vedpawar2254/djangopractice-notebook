module.exports = {
  // corePlugins: {
  //   preflight: false,
  // },
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false, //true for production build
    content: ["../**/templates/*.html", "../**/templates/**/*.html"],
  },
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
};
