# Steps to Add Tailwind CSS

  1. Download Tailwind CLI

  curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
  chmod +x tailwindcss-linux-x64
  mv tailwindcss-linux-x64 tailwindcss

  2. Create tailwind.config.js

  /** @type {import('tailwindcss').Config} */
  module.exports = {
    content: [
      './apps/**/templates/**/*.html',
      './static/js/**/*.js',
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }

  3. Create static/css/input.css

  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  4. Add to Makefile

  tw-build:
  	./tailwindcss -i static/css/input.css -o static/css/tailwind.css --minify

  tw-watch:
  	./tailwindcss -i static/css/input.css -o static/css/tailwind.css --watch

  5. Update _layout.html

  Replace the Pico CSS link with:
  <link rel="stylesheet" href="{% static 'css/tailwind.css' %}">

  6. Add to .gitignore

  tailwindcss
  (Keep the binary out of git - download during setup)

  7. Run the build

  make tw-build

  Do you want me to implement any or all of these steps?
