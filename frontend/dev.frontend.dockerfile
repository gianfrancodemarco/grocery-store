# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:18 as build-stage

WORKDIR /app

COPY package.json ./

RUN npm install
ARG FRONTEND_ENV=dev

ENV VUE_APP_ENV=${FRONTEND_ENV}

# Comment out the next line to disable tests
#RUN npm run test:unit

RUN chown -R node:node /app/node_modules

COPY ./ ./

ENTRYPOINT npm run serve