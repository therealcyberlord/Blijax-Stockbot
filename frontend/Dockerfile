FROM node:14

WORKDIR /app1

COPY . .

RUN npm install

ENTRYPOINT ["npm"]
CMD ["run", "dev"]

EXPOSE 3000