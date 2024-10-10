# Use Node.js official image as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the Next.js application
CMD ["npm", "run", "dev"]
