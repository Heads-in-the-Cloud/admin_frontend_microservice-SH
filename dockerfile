FROM 026390315914.dkr.ecr.us-west-2.amazonaws.com/utopia_frontend_base_image-sh

WORKDIR /app
COPY . /app

EXPOSE 5000
