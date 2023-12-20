module.exports = {
  apps: [
    {
      name: "Flask",
      args: "--app main run",
      cwd: "/home/admin/wax-server/wax",
      script: "/usr/local/bin/flask",
      env: {},
      exec_interpreter: "none",
      },
    {
      name: "Ngrok",
      args: "http --hostname=wax.eu.ngrok.io 5000",
      cwd: "/home/admin/wax-server",
      script: "/usr/local/bin/ngrok",
      env: {},
    },
  ],
};
