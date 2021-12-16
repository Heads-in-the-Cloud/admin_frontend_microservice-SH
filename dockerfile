FROM 026390315914.dkr.ecr.us-west-2.amazonaws.com/utopia_frontend_base_image-sh

# Changing working directory to the system user's home repository
WORKDIR /home/utopian/app
# Copying the necessary files into the application folder
COPY templates templates
COPY app.py config.py entry_script.sh forms.py routes.py tests.py ./
# Ensuring that the entry_script has execution permissions
RUN chmod +x entry_script.sh

# Setting the FLASK_APP environmental variable
ENV FLASK_APP app.py

# Ensuring that the system user has the appropriate permissions to run the application
RUN chown -R utopian:utopian ./
# Switching to the system user to run the image
USER utopian

# Exposing port 5000 for Flask interactions
EXPOSE 5000

# Setting the entry_script as the image's entrypoint
ENTRYPOINT ["/home/utopian/app/entry_script.sh"]