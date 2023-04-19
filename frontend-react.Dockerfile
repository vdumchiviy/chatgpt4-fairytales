FROM node:13

WORKDIR /app
COPY ./frontend_react .
RUN npm install
RUN npm run build
CMD ["npm", "start"]

# docker build -t fairytales_front_react:latest -f frontend-react.Dockerfile .
# docker tag fairytales_front_react vdumchiviy/fairytales_front_react 
# docker push vdumchiviy/fairytales_front_react:latest