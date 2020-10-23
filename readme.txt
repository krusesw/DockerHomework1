Image is saved with docker save
	 cmd used: sudo docker save -o "/home/kruse/Desktop/Docker Project/DHWImage" dhw1
	 
	 
To load this image from backup file use docker load
	 
	 
Image is ran by using docker run, must mount a directory to /home/data
	cmd used: sudo docker run --name dhw1Container --mount type=bind,source=/home/kruse/data,targer=/home/data dhw1
	
Image build using docker build . --tag dhw1
