export default module.exports = {
  apps: [
    {
      name: "Flask",
      args: "--app main run",
      cwd: "/home/admin/wax-server",
      script: "/usr/bin/local/flask",
      env: {},
    },
    {
      name: "Ngrok",
      args: "http --hostname=YOURSUBDOMAINHERE.ngrok.io 5000",
      cwd: "/home/admin/wax-server",
      script: "/usr/bin/local/ngrok",
      env: {},
    },
  ],
};
