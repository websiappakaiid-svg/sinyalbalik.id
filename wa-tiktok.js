// Blog: TikTok di iPhone nahan link WA, jadi arahin ke panduan di halaman depan (pesannya ikut kebawa)
(function(){
  var ua=navigator.userAgent;
  if(!(/musical_ly|bytedancewebview|tiktok|trill/i.test(ua)&&/iPhone|iPad|iPod/.test(ua)))return;
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href*="wa.me/"]');if(!a)return;
    e.preventDefault();
    var t='';try{t=new URL(a.href).searchParams.get('text')||'';}catch(x){}
    try{sessionStorage.setItem('sbMsg','b|'+(t||'Halo Admin SinyalBalik, saya mau tanya dulu'));}catch(x){}
    location.href='/?wa=b';
  });
})();
