# Pi Setup Guide — thvarzil.dev

One-time setup steps to run on a fresh Raspberry Pi OS (64-bit recommended).

---

## 1. System packages

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y nginx postgresql postgresql-contrib python3-venv python3-pip ddclient certbot python3-certbot-nginx
```

---

## 2. Postgres

```bash
sudo -u postgres psql <<EOF
CREATE USER portfolio WITH PASSWORD 'your-password';
CREATE DATABASE portfolio OWNER portfolio;
EOF
```

---

## 3. Clone the repo

```bash
sudo mkdir -p /srv/portfolio
sudo chown pi:pi /srv/portfolio
git clone https://github.com/thvarzil/portfolio.git /srv/portfolio
```

---

## 4. Python virtualenv

```bash
python3 -m venv /srv/portfolio/venv
/srv/portfolio/venv/bin/pip install -r /srv/portfolio/backend/requirements.txt
```

---

## 5. Environment file

```bash
sudo mkdir -p /etc/portfolio
sudo cp /srv/portfolio/deploy/env.example /etc/portfolio/env
sudo chown root:pi /etc/portfolio/env
sudo chmod 640 /etc/portfolio/env
sudo nano /etc/portfolio/env   # fill in SECRET_KEY and POSTGRES_PASSWORD
```

Generate a secret key:
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 6. Log directory

```bash
sudo mkdir -p /var/log/portfolio
sudo chown pi:www-data /var/log/portfolio
sudo chmod 770 /var/log/portfolio
```

---

## 7. Django setup

```bash
cd /srv/portfolio/backend
/srv/portfolio/venv/bin/python manage.py migrate
/srv/portfolio/venv/bin/python manage.py collectstatic --noinput
/srv/portfolio/venv/bin/python manage.py createsuperuser
```

---

## 8. Gunicorn systemd service

```bash
sudo cp /srv/portfolio/deploy/portfolio-gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable portfolio-gunicorn
sudo systemctl start portfolio-gunicorn
sudo systemctl status portfolio-gunicorn   # should show active (running)
```

---

## 9. nginx

```bash
sudo cp /srv/portfolio/deploy/thvarzil.dev.nginx.conf /etc/nginx/sites-available/thvarzil.dev
sudo ln -s /etc/nginx/sites-available/thvarzil.dev /etc/nginx/sites-enabled/thvarzil.dev
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

---

## 10. Router setup

In your router admin panel:
- Give the Pi a **static DHCP reservation** (bind its MAC address to a fixed local IP, e.g. `192.168.1.100`)
- **Port forward** TCP ports 80 and 443 to that local IP

---

## 11. Dynamic DNS (Hover)

1. Log into Hover → your domain → DNS → enable DDNS for `thvarzil.dev`, `www.thvarzil.dev`, `thvarzil.com`, `www.thvarzil.com`
2. Configure ddclient:

```bash
sudo cp /srv/portfolio/deploy/ddclient.conf /etc/ddclient.conf
sudo nano /etc/ddclient.conf   # fill in your Hover username and password
sudo systemctl enable ddclient
sudo systemctl start ddclient
```

---

## 12. TLS certificate (Let's Encrypt)

Wait until your domain is resolving to your Pi's public IP (check with `dig thvarzil.dev`), then:

```bash
sudo certbot --nginx -d thvarzil.dev -d www.thvarzil.dev -d thvarzil.com -d www.thvarzil.com
```

Certbot will auto-renew via a systemd timer — no action needed.

---

## Deploying updates

From your dev machine, push to git. Then on the Pi:

```bash
/srv/portfolio/deploy/deploy.sh
```

Or set up a post-receive git hook to run it automatically.
