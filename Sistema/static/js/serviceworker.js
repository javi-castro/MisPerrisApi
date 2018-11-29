var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/mascota',
        '/api/v1/mascota',
        '/nosotros',
        '/contacto',
        '/login',
        '/logout',
        '/',
      ]);
    })
  );
});

self.addEventListener('activate', event => {
  var keepList = [CACHE_NAME];

  event.waitUntil(
      caches.keys().then(cacheNameList => {
          return Promise.all(cacheNameList.map(cacheName => { 
              if (keepList.indexOf(cacheName) === -1) {
                  return caches.delete(cacheName);
              }
          }));
      })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
