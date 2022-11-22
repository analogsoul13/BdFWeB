/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html', './node_modules/tw-elements/dist/js/*.js'],
  theme: {
    screens:{
      sm: '480px',
      md: '786px',
      lg: '976px',
      xl: '1440px'

    },
    extend: {
      backgroundImage: {
        'bg-home': "url(.static/img/bg-tablet-pattern.svg')",
      },
      colors:{
        brightRed: 'rgb(201,19,55)',
        brightRedLight: 'rgb(233,22,64)',
        brightRedSupLight: 'rgb(236,50,87)',
        darkBlue: '#0f172a',
        darkGrayishBlue: 'hsl(227, 12%, 61%)',
        veryDarkBlue: 'hsl(223, 12%, 13%)',
        veryPaleRed: 'hsl(13, 100%, 96%)',
        veryLightGray: 'hsl(0, 0%, 98%)',
      }
    },
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ],
}
