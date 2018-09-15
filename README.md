# Extra Life Raspberry PI Screamer

This project connects to the Extra Life/Donor Drive provided endpoints to query if there has been a new donation. On setup it makes a request to the endpoint and captures the etag.

The DonationService then makes the same request with that etag etag as the value of 'If-none-match' in the request header every 15 seconds. If the result is 200, the etag is updated and the event is propagated to the event handler. All other http response statuses are ignored.

**NOTE: Because it needs to configure the endpoint and get the etag on setup, the earliest an event will trigger is 15 seconds after the initial run of the program, debug or not.**

# Dependencies
PHUE Python Library for Phillips Hue Light Bulbs - https://github.com/studioimaginaire/phue

## Debug Mode

In debug mode, the 304 NOT_MODIFIED response codes will also propagate an event to the handler. This will help testing of the handlers even if there are no new donations.

## Provided Event Handlers

### Screamer
This handler configures a philips hue controller connected to a raspberry pi with a baked in IP of 10.0.13.23

When it receives an event, it selects a video from the set ['Boo1.mp4', 'Boo2.mp4', 'Boo3.mp4', 'Boo4.mp4', 'Boo5.mp4'] and plays the mp4. It also sets off a pre-configured set of strobe effects.

### DonationPrinter
This handler will print 'Dontation recieved alert' to the console .

## Endpoint
The endpoint hit is the team api for The Dream Cast team. It is baked into extraLifeScreamer.py and passed into the DonationService class in the screamer module.

Endpoint: www.extra-life.org/api/teams/38776

## Usage

`python test.py [printer|screamer] [--debug]`

 - Specify printer to use the DonationPrinter handler
 - Specify screamer to use the Screamer handler. 
	  - If both are specified, Screamer is used.
  - Specify --debug to enable debug mode.

## Provided Launch Scripts
A set of pre-written linux shell scripts are provided for each of launch.
`screamerLaunch.sh` - Launches the screamer with the Screamer handler, not in debug mode. Good for game day.
`screamerLaunch.sh` - Launches the screamer with the screamer handler in debug mode. Good for making sure the configuration of the philips hue is working. (It will essentially trigger the strobe/video every 15 seconds).
`screamerLaunchDebugPrint.sh` - Launches the screamer with the DonationPrinter handler in debug mode. Good for checking the behaviour of DonationService.
