export function isTokenValid() {
  const token = localStorage.getItem('token');

  if (!token) {
    return false;
  }

  const expiry = JSON.parse(atob(token.split('.')[1])).exp;
  const now = Math.floor(Date.now() / 1000);

  return expiry > now;
}
