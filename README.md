# auth-server-demo

This is a simple demonstration of some aspects of https://tools.ietf.org/html/rfc6749 and https://tools.ietf.org/html/rfc7662.

In this demo, we are developing:
- OAuth 2.0 Authorization Server
- Two resource servers
- One client app that is accessing resources from both resource servers.

## Installation

Make sure you have docker and `docker-compose` installed from https://docs.docker.com/install/ and https://docs.docker.com/compose/install/.

We will have 4 `docker-compose`'s `yml` files to create 4 "separate machines": one Auth Server, two Resource Servers and one Client App.

### Preparing environment variables

Create `.env` file and put this content:
```
DOCKER_0_HOST=

OAUTH2_SERVER_POSTGRES_EXTERNAL_PORT=5433
OAUTH2_SERVER_POSTGRES_USER=postgres
OAUTH2_SERVER_POSTGRES_PASSWORD=
OAUTH2_SERVER_WEB_EXTERNAL_PORT=8000

RESOURCE_SERVER_1_WEB_EXTERNAL_PORT=8001
RESOURCE_SERVER_2_WEB_EXTERNAL_PORT=8002

CLIENT_APP_ID=
CLIENT_APP_SECRET=
CLIENT_APP_WEB_EXTERNAL_PORT=8003
```

You can customize the values later.

There are still 3 values unfilled.

`DOCKER_0_HOST` should be filled with the IP address of `docker0`. You can get the
IP address of `docker0` using the `ifconfig` command.

You will fill the values for `CLIENT_APP_ID` and `CLIENT_APP_SECRET` later when you created the application data on the Auth Server.

### Installing the Auth Server

Build the container:
```
$ docker-compose -f docker-compose-oauth2.yml build
```

Prepare initial data and create an admin user of the Auth User:
```
$ docker-compose -f docker-compose-oauth2.yml run --rm oauth2_server ./migrate_data.sh
$ docker-compose -f docker-compose-oauth2.yml run --rm oauth2_server ./create_superuser.sh
```

Run the Auth Server:
```
$ docker-compose -f docker-compose-oauth2.yml up
```

Now that the Auth Server is up, you can add clients to it. Let's add one client and use the generate keys to fill
CLIENT_ID and CLIENT_SECRET in the `.env` file:
1. Open http://localhost:8000/o/applications/register/. If you are asked to login, please use the admin account you have just created.
2. Enter the `Name` field with anything you want.
3. `Client type` is `Confidential`.
4. `Authorization grant type` is `Authorization code`.
5. `Redirect uris` is `http://localhost:8003/auth/token/exchange/`.

### Installing the two Resource Servers

run the containers:
```
$ docker-compose -f docker-compose-resource-1.yml up
$ docker-compose -f docker-compose-resource-2.yml up
```

### Installing the Client App

run the container:
```
$ docker-compose -f docker-compose-client.yml up
```

Create another user of the Auth Server that represent a user that is using the Client App:
1. Open http://localhost:8000/admin/auth/user/add/. If you are asked to login, please use the admin username that you have created before.
2. Fill the username and password fields let's call this new user as `user1`.
3. Logout from the admin account.

## Run the Demo

1. Open the Client App at http://localhost:8003/. The `Access Token` should still be empty.
2. Click `Login to get a valid access token`. You will be asked to login. Please login with the username and password of `user1`.
3. Authorization page will be displayed. Click `Authorize`.
4. The browser should now be redirected back to the demo page at http://localhost:8003/.
5. Now the `Access Token` field is filled with a valid value.
6. Click `Access Resources`. If you see "Resource Server 1" and "Resource Server 2" texts are displayed, it means resources
   are successfully loaded from the two Resource Servers.

You can now do some experiments by changing or removing value of access token.
