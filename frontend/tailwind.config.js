// tailwind.config.cjs

/** @type {import('tailwindcss').Config} */
// eslint-disable-next-line no-undef
module.exports = {
  content: [ // tell Tailwind which files to track
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // all js and ts files in src/
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}