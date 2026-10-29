/* Sanchari site scripts */
/* Account store: user, bookings and wishlist kept in this browser (localStorage).
   Passwords are never stored. Replace with a real backend before taking live payments. */
window.SAN = (function () {
  const K = { u: 'san_user', b: 'san_bookings', w: 'san_wishlist' };
  const get = (k, d) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } };
  const set = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  return {
    user: () => get(K.u, null),
    setUser: u => set(K.u, Object.assign({}, get(K.u, {}) || {}, u)),
    logout: () => { try { localStorage.removeItem(K.u); } catch (e) {} },
    bookings: () => get(K.b, []),
    addBooking: b => { const l = get(K.b, []).filter(x => x.inv !== b.inv); l.unshift(b); set(K.b, l.slice(0, 50)); },
    wishlist: () => get(K.w, []),
    toggleWish: slug => { let l = get(K.w, []); const on = !l.includes(slug); l = on ? [slug].concat(l) : l.filter(x => x !== slug); set(K.w, l); return on; },
    newInvoiceNo: () => { const n = new Date(); return 'SAN-' + n.getFullYear() + String(n.getMonth() + 1).padStart(2, '0') + String(n.getDate()).padStart(2, '0') + '-' + Math.floor(1000 + Math.random() * 9000); },
    first: u => ((u && u.name) || 'Traveller').trim().split(' ')[0]
  };
})();

/* Logged in: header "Login" buttons become a link to My Account */
(function () {
  const u = SAN.user(); if (!u) return;
  document.querySelectorAll('.login[data-auth], .m-login[data-auth]').forEach(b => {
    const a = document.createElement('a'); a.href = 'account.html'; a.className = b.className + ' is-in';
    a.innerHTML = b.classList.contains('login') ? b.querySelector('svg').outerHTML + 'Hi, ' + SAN.first(u).replace(/[<>&]/g, '') : 'My Account';
    b.replaceWith(a);
  });
})();

(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Mobile nav
  const mBtn = $('.menu-btn'), mNav = $('#mnav');
  if (mBtn && mNav) {
    mBtn.addEventListener('click', () => mNav.classList.toggle('open'));
    $$('a', mNav).forEach(a => a.addEventListener('click', () => mNav.classList.remove('open')));
  }

  // Swap in real photos when they load; keep the local dummy image otherwise
  $$('img[data-real]').forEach(img => {
    const t = new Image();
    t.onload = () => { img.src = img.dataset.real; };
    t.src = img.dataset.real;
  });
  $$('[data-bg-real]').forEach(el => {
    const u = el.dataset.bgReal, t = new Image();
    t.onload = () => { el.style.backgroundImage = 'url("' + u + '")'; };
    t.src = u;
  });

  // Simple forms: show a thank-you message
  $$('form[data-ok]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const ok = document.getElementById(f.dataset.ok);
    if (ok) ok.style.display = 'block';
    f.reset();
  }));

  // Home hero slider
  const slides = $$('.slide');
  if (slides.length > 1) {
    const dots = $$('.dots button');
    let i = 0, timer;
    const show = n => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle('on', k === i));
      dots.forEach((d, k) => d.classList.toggle('on', k === i));
    };
    const play = () => { clearInterval(timer); timer = setInterval(() => show(i + 1), 6000); };
    dots.forEach((d, k) => d.addEventListener('click', () => { show(k); play(); }));
    play();
  }

  // Home search: pick an Activity first, then its destinations appear
  const hs = $('#homeSearch');
  if (hs) {
    const act = $('#hAct'), dest = $('#hDest'), errEl = $('#hsErr');
    const HD = JSON.parse(($('#hsData') || {}).textContent || '{}');
    const esc = t => String(t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    const fill = () => {
      const d = HD[act.value];
      errEl.textContent = ''; act.classList.remove('is-err');
      if (!d) { dest.innerHTML = '<option value="all">Select an activity first</option>'; dest.disabled = true; dest.closest('.field').classList.add('is-off'); return; }
      dest.innerHTML = '<option value="all">' + esc(d.all) + '</option>' + d.groups.map(g => {
        const o = g[1].map(x => '<option value="' + esc(x[0]) + '">' + esc(x[1]) + '</option>').join('');
        return g[0] ? '<optgroup label="' + esc(g[0]) + '">' + o + '</optgroup>' : o;
      }).join('');
      dest.disabled = false; dest.closest('.field').classList.remove('is-off');
      dest.classList.remove('flash'); void dest.offsetWidth; dest.classList.add('flash');
    };
    act.addEventListener('change', fill); fill();
    hs.addEventListener('submit', e => {
      e.preventDefault();
      const map = { temple: 'temple-tours.html', adventure: 'adventure-tours.html', wellness: 'wellness-tours.html' };
      if (!map[act.value]) { errEl.textContent = 'Please choose an activity to see destinations.'; act.classList.add('is-err'); act.focus(); return; }
      location.href = map[act.value] + (dest.value !== 'all' ? '?region=' + encodeURIComponent(dest.value) : '') + '#tours';
    });
  }

  // Tour listing filters
  const grid = $('#grid');
  if (grid) {
    const cards = $$('.card', grid), cnt = $('#cnt'), empty = $('#empty');
    const sDest = $('#sDest'), sDur = $('#sDur'), sBud = $('#sBudget'), sort = $('#sort'), sType = $('#sType');
    let style = 'all', circuit = 'all';
    let region = new URLSearchParams(location.search).get('region') || 'all';
    if (!$$('.chip').some(c => c.dataset.f === region) && !cards.some(c => c.dataset.region === region || c.dataset.zone === region)) region = 'all';
    const render = () => {
      const dur = sDur ? sDur.value : 'all', bud = sBud ? sBud.value : 'all';
      let shown = cards.filter(c => {
        const d = +c.dataset.days, p = +c.dataset.price;
        if (region !== 'all' && c.dataset.region !== region && c.dataset.zone !== region) return false;
        if (style !== 'all' && !(c.dataset.styles || '').split(' ').includes(style)) return false;
        if (circuit !== 'all' && !(c.dataset.circuits || '').split(' ').includes(circuit)) return false;
        if (dur !== 'all') { const [a, b] = dur.split('-').map(Number); if (d < a || d > b) return false; }
        if (bud !== 'all' && p >= +bud) return false;
        return true;
      });
      const key = { featured: c => +c.dataset.order, low: c => +c.dataset.price, high: c => -c.dataset.price, days: c => +c.dataset.days }[sort ? sort.value : 'featured'];
      shown.sort((a, b) => key(a) - key(b));
      cards.forEach(c => c.style.display = 'none');
      shown.forEach(c => { c.style.display = ''; grid.appendChild(c); });
      const note = $('.grid-note', grid); if (note) grid.appendChild(note);
      cnt.textContent = shown.length;
      empty.style.display = shown.length ? 'none' : 'block';
    };
    const ycBar = $('#ycBar'), ycName = $('#ycName');
    const setCircuit = k => {
      circuit = k;
      $$('.yc').forEach(y => y.classList.toggle('on', y.dataset.c === k));
      if (ycBar) { ycBar.hidden = k === 'all'; const y = $$('.yc').find(y => y.dataset.c === k); if (y && ycName) ycName.textContent = y.dataset.name + ' tours'; }
    };
    const setRegion = r => {
      region = r;
      $$('.chip').forEach(ch => ch.classList.toggle('on', ch.dataset.f === r));
      if (sDest) sDest.value = r;
      render();
    };
    $$('.chip').forEach(ch => ch.addEventListener('click', () => { setCircuit('all'); setRegion(ch.dataset.f); }));
    $$('.yc').forEach(y => y.addEventListener('click', e => { e.preventDefault(); setCircuit(y.dataset.c); setRegion('all'); $('#tours').scrollIntoView({ behavior: 'smooth' }); }));
    if ($('#ycClear')) $('#ycClear').addEventListener('click', () => { setCircuit('all'); render(); });
    const styleSel = $('#styleSel');
    const setStyle = st => {
      style = st;
      $$('.seg-b').forEach(b => b.classList.toggle('on', b.dataset.s === st));
      if (sType) sType.value = st;
      if (styleSel) styleSel.value = st;
      render();
    };
    if (styleSel) styleSel.addEventListener('change', () => setStyle(styleSel.value));
    $$('.seg-b').forEach(b => b.addEventListener('click', () => setStyle(b.dataset.s)));
    const qs = new URLSearchParams(location.search).get('style');
    if (qs && ['individual', 'group'].includes(qs)) style = qs;
    $$('.seg-b').forEach(b => b.classList.toggle('on', b.dataset.s === style));
    if (sType) sType.value = style;
    if (styleSel) styleSel.value = style;
    if (sort) sort.addEventListener('change', render);
    const sf = $('#searchForm');
    if (sf) sf.addEventListener('submit', e => { e.preventDefault(); if (sType) { style = sType.value; $$('.seg-b').forEach(b => b.classList.toggle('on', b.dataset.s === style)); if (styleSel) styleSel.value = style; } setRegion(sDest.value); $('#tours').scrollIntoView({ behavior: 'smooth' }); });
    window.resetFilters = () => { setCircuit('all'); if (sDur) sDur.value = 'all'; if (sBud) sBud.value = 'all'; style = 'all'; $$('.seg-b').forEach(b => b.classList.toggle('on', b.dataset.s === 'all')); if (sType) sType.value = 'all'; if (styleSel) styleSel.value = 'all'; setRegion('all'); };
    const qc = new URLSearchParams(location.search).get('circuit');
    if (qc && $$('.yc').some(y => y.dataset.c === qc)) setCircuit(qc);
    setRegion(region);
  }

  // Booking card
  const book = $('#bookForm');
  if (book) {
    const price = +book.dataset.price, pax = { a: +($('#pa') || {}).textContent || 1, c: 0 };
    const dt = $('#bDate'); if (dt) dt.min = new Date().toISOString().split('T')[0];
    const upd = () => { $('#tot').textContent = '₹' + (price * (pax.a + pax.c)).toLocaleString('en-IN'); };
    $$('[data-pax]', book).forEach(b => b.addEventListener('click', () => {
      const k = b.dataset.pax, d = +b.dataset.d;
      pax[k] = Math.max(k === 'a' ? 1 : 0, Math.min(20, pax[k] + d));
      $('#p' + k).textContent = pax[k]; upd();
    }));
    const me = SAN.user();
    if (me) { [['bName', 'name'], ['bPhone', 'phone'], ['bEmail', 'email']].forEach(([id, k]) => { const el = $('#' + id); if (el && !el.value && me[k]) el.value = me[k]; }); }
    book.addEventListener('submit', e => {
      e.preventDefault();
      const inv = SAN.newInvoiceNo();
      const st = book.querySelector('input[name="bStyle"]:checked');
      const q = new URLSearchParams({ tour: book.dataset.slug, date: dt ? dt.value : '', a: pax.a, c: pax.c,
        style: st ? st.value : ((book.querySelector('input[name="bStyleFixed"]') || {}).value || 'group'), name: ($('#bName') || {}).value || '', phone: ($('#bPhone') || {}).value || '',
        email: ($('#bEmail') || {}).value || '', inv });
      SAN.addBooking({ inv, tour: book.dataset.slug, date: q.get('date'), a: pax.a, c: pax.c, style: q.get('style'),
        name: q.get('name'), phone: q.get('phone'), email: q.get('email'), created: new Date().toISOString() });
      if (!SAN.user() && q.get('name')) SAN.setUser({ name: q.get('name'), phone: q.get('phone'), email: q.get('email') });
      location.href = 'invoice.html?' + q.toString();
    });
    upd();
  }

  // Itinerary expand/collapse
  const tg = $('#toggleDays');
  if (tg) tg.addEventListener('click', () => {
    const open = tg.textContent.includes('Expand');
    $$('.day').forEach(d => d.open = open);
    tg.textContent = open ? 'Collapse all' : 'Expand all';
  });

  // Share & wishlist
  const sh = $('#shareBtn');
  if (sh) sh.addEventListener('click', () => {
    if (navigator.share) navigator.share({ title: document.title, url: location.href }).catch(() => {});
    else if (navigator.clipboard) navigator.clipboard.writeText(location.href);
  });
  const wl = $('#wishBtn');
  if (wl) { const s = wl.dataset.slug, mark = on => { wl.classList.toggle('on', on); wl.setAttribute('aria-pressed', on); wl.setAttribute('aria-label', on ? 'Saved to wishlist' : 'Save to wishlist'); };
    mark(SAN.wishlist().includes(s)); wl.addEventListener('click', () => mark(SAN.toggleWish(s))); }

  // Active tab while scrolling a tour page
  const tabs = $$('.d-tabs a');
  if (tabs.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) tabs.forEach(t => t.classList.toggle('on', t.getAttribute('href') === '#' + e.target.id));
    }), { rootMargin: '-160px 0px -60% 0px' });
    tabs.forEach(t => { const el = $(t.getAttribute('href')); if (el) io.observe(el); });
  }
})();

/* Login / Sign up popup */
(function () {
  const m = document.getElementById('auth'); if (!m) return;
  const $ = (s, r = m) => r.querySelector(s), $$ = (s, r = m) => [...r.querySelectorAll(s)];
  let last = null;
  const show = tab => {
    $$('.auth-pane').forEach(p => p.hidden = true);
    $$('.auth-tabs button').forEach(b => { const on = b.dataset.tab === tab; b.classList.toggle('on', on); b.setAttribute('aria-selected', on); });
    $('.auth-tabs').hidden = false;
    $('#pane-' + tab).hidden = false;
    $$('.auth-err').forEach(e => e.textContent = '');
    const f = $('#pane-' + tab + ' input'); if (f) setTimeout(() => f.focus(), 60);
  };
  const open = tab => {
    last = document.activeElement; m.hidden = false; document.body.classList.add('no-scroll');
    requestAnimationFrame(() => m.classList.add('in')); show(tab || 'login');
    const nav = document.getElementById('mnav'); if (nav) nav.classList.remove('open');
  };
  const close = () => {
    if (document.getElementById('acApp') && SAN.user() && document.getElementById('acApp').hidden) { location.reload(); return; }
    m.classList.remove('in'); document.body.classList.remove('no-scroll');
    setTimeout(() => { m.hidden = true; $$('form', m).forEach(f => f.reset()); }, 200);
    if (last) last.focus();
  };
  document.querySelectorAll('[data-auth]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); open(b.dataset.auth); }));
  $$('[data-close]').forEach(b => b.addEventListener('click', close));
  $$('[data-tab]').forEach(b => b.addEventListener('click', () => show(b.dataset.tab)));
  document.addEventListener('keydown', e => {
    if (m.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'Tab') { // keep focus inside the popup
      const f = $$('button, input, a[href]').filter(x => x.offsetParent !== null);
      if (!f.length) return;
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
    }
  });
  $$('.pw-t').forEach(b => b.addEventListener('click', () => {
    const i = document.getElementById(b.dataset.pw), sh = i.type === 'password';
    i.type = sh ? 'text' : 'password'; b.classList.toggle('on', sh); b.setAttribute('aria-label', sh ? 'Hide password' : 'Show password');
  }));
  const done = (title, text) => {
    $$('.auth-pane').forEach(p => p.hidden = true); $('.auth-tabs').hidden = true;
    $('#doneTitle').textContent = title; $('#doneText').textContent = text; $('#pane-done').hidden = false;
  };
  const err = (f, msg, el) => { $('.auth-err', f).textContent = msg; if (el) el.focus(); };
  $('#pane-login').addEventListener('submit', e => {
    e.preventDefault(); const f = e.target, u = $('#lEmail'), p = $('#lPass');
    if (!u.value.trim()) return err(f, 'Please enter your email or phone number.', u);
    if (p.value.length < 8) return err(f, 'Password must be at least 8 characters.', p);
    const id = u.value.trim(), prev = SAN.user() || {}, isMail = id.includes('@');
    const nm = prev.name || (isMail ? id.split('@')[0].replace(/[._-]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase()) : 'Traveller');
    SAN.setUser(Object.assign({ name: nm }, isMail ? { email: id } : { phone: id }));
    done('Welcome back, ' + SAN.first(SAN.user()) + '!', 'You’re logged in. Your bookings, invoices and saved tours are in My Account.');
  });
  $('#pane-signup').addEventListener('submit', e => {
    e.preventDefault(); const f = e.target;
    const n = $('#sName'), ph = $('#sPhone'), em = $('#sEmail'), p1 = $('#sPass'), p2 = $('#sPass2'), t = $('#sTerms');
    if (!n.value.trim()) return err(f, 'Please enter your full name.', n);
    if (ph.value.replace(/\D/g, '').length < 10) return err(f, 'Please enter a valid phone number.', ph);
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value)) return err(f, 'Please enter a valid email address.', em);
    if (p1.value.length < 8) return err(f, 'Password must be at least 8 characters.', p1);
    if (p1.value !== p2.value) return err(f, 'Passwords don’t match.', p2);
    if (!t.checked) return err(f, 'Please accept the Terms & Privacy Policy.', t);
    SAN.setUser({ name: n.value.trim(), phone: ph.value.trim(), email: em.value.trim() });
    done('Account created!', 'Welcome to Sanchari, ' + n.value.trim().split(' ')[0] + '. Your account is ready.');
  });
  $('[data-forgot]').addEventListener('click', () => {
    const u = $('#lEmail');
    if (!u.value.trim()) return err($('#pane-login'), 'Enter your email or phone above, then click “Forgot password?”', u);
    done('Check your inbox', 'If an account exists for ' + u.value.trim() + ', we’ve sent a link to reset your password.');
  });
})();

/* Popular journeys reels carousel */
(function () {
  const track = document.getElementById('reelTrack'); if (!track) return;
  const reels = [...track.querySelectorAll('.reel')], dotsWrap = document.getElementById('reelDots');
  const step = () => (reels[0].getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 20));
  document.querySelectorAll('.reel-arrow').forEach(b => b.addEventListener('click', () => {
    track.scrollBy({ left: step() * (+b.dataset.dir) * (window.innerWidth > 760 ? 2 : 1), behavior: 'smooth' });
  }));
  // dots
  reels.forEach((r, i) => { const d = document.createElement('button'); d.type = 'button'; d.setAttribute('aria-label', 'Go to journey ' + (i + 1));
    d.addEventListener('click', () => r.scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' })); dotsWrap.appendChild(d); });
  const dots = [...dotsWrap.children];
  // "playing" reel = the one most in view; it zooms and its progress bar runs
  // video reels: stream only the active one (muted). The photo shows until the clip is actually playing;
  // if the clip can't load, the card stays a photo reel. Each clip plays an 8-second window.
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const syncVideos = () => reels.forEach(r => { const v = r.querySelector('video'); if (!v || v.dataset.failed) return;
    if (r.classList.contains('playing') && !reduce) {
      if (!v.src) { v.src = v.dataset.src; v.preload = 'auto'; }
      const st = +v.dataset.start || 0;
      if (v.currentTime < st || v.currentTime > st + (+v.dataset.len || 8)) { try { v.currentTime = st; } catch (e) {} }
      const p = v.play(); if (p && p.catch) p.catch(() => {});
    } else if (v.src) v.pause(); });
  reels.forEach((r, i) => { const v = r.querySelector('video'); if (!v) return;
    const st = () => +v.dataset.start || 0, len = () => +v.dataset.len || 8;
    v.addEventListener('playing', () => r.classList.add('is-video', 'vid-on'));
    v.addEventListener('error', () => { v.dataset.failed = '1'; r.classList.remove('is-video', 'vid-on'); v.removeAttribute('src'); });
    v.addEventListener('timeupdate', () => {
      const p = Math.min(100, Math.max(0, (v.currentTime - st()) / len() * 100));
      r.style.setProperty('--vp', p + '%');
      if (v.currentTime >= st() + len()) {
        // end of the clip window: advance, or replay if the visitor is hovering this reel
        if (!paused && r.classList.contains('playing')) { v.pause(); goNext(i); } else { v.currentTime = st(); }
      }
    });
    v.addEventListener('ended', () => { if (!paused && r.classList.contains('playing')) goNext(i); else { v.currentTime = st(); v.play().catch(() => {}); } });
  });
  const setPlaying = () => {
    const tr = track.getBoundingClientRect(); let best = null, bestScore = -1;
    reels.forEach(r => { const b = r.getBoundingClientRect(); const vis = Math.max(0, Math.min(b.right, tr.right) - Math.max(b.left, tr.left)); if (vis > bestScore + 1) { bestScore = vis; best = r; } });
    reels.forEach((r, i) => { r.classList.toggle('playing', r === best); dots[i].classList.toggle('on', r === best); });
    syncVideos();
  };
  let t; track.addEventListener('scroll', () => { clearTimeout(t); t = setTimeout(setPlaying, 80); });
  reels.forEach(r => r.addEventListener('mouseenter', () => { reels.forEach(x => x.classList.toggle('playing', x === r)); dots.forEach((d, i) => d.classList.toggle('on', reels[i] === r)); syncVideos(); }));
  setPlaying();
  // when a reel's progress finishes, move on to the next one (auto-play, paused on hover/focus)
  let paused = false;
  track.addEventListener('mouseenter', () => paused = true); track.addEventListener('mouseleave', () => paused = false);
  track.addEventListener('focusin', () => paused = true); track.addEventListener('focusout', () => paused = false);
  function goNext(i) {
    const next = reels[(i + 1) % reels.length];
    if (i + 1 >= reels.length) track.scrollTo({ left: 0, behavior: 'smooth' });
    else track.scrollTo({ left: next.offsetLeft - reels[0].offsetLeft, behavior: 'smooth' });
    reels.forEach(x => x.classList.toggle('playing', x === next)); dots.forEach((d, k) => d.classList.toggle('on', reels[k] === next));
    syncVideos();
  }
  reels.forEach((r, i) => r.querySelector('.reel-bar span').addEventListener('animationend', () => {
    if (paused || !r.classList.contains('playing') || r.classList.contains('is-video')) return;
    goNext(i);
  }));
  // like & share
  track.querySelectorAll('.reel-like').forEach(b => {
    const s = b.dataset.slug, mark = on => { b.setAttribute('aria-pressed', on); b.classList.toggle('on', on); const t = b.querySelector('small'); if (t) t.textContent = on ? 'Saved' : 'Save'; };
    mark(SAN.wishlist().includes(s));
    b.addEventListener('click', e => { e.preventDefault(); mark(SAN.toggleWish(s)); });
  });
  track.querySelectorAll('.reel-share').forEach(b => b.addEventListener('click', e => {
    e.preventDefault(); const url = new URL(b.dataset.url, location.href).href;
    if (navigator.share) navigator.share({ title: document.title, url }).catch(() => {});
    else if (navigator.clipboard) { navigator.clipboard.writeText(url); b.querySelector('small').textContent = 'Copied'; setTimeout(() => b.querySelector('small').textContent = 'Share', 1500); }
  }));
})();

/* Custom packages video popup (mp4 file or YouTube link) */
(function () {
  const m = document.getElementById('vmodal'); if (!m) return;
  const frame = document.getElementById('vmFrame');
  const soon = '<div class="vm-soon"><b>Our journey film is coming soon</b><span>Meanwhile, talk to our team about a custom trip.</span><a class="btn btn-gold" href="contact.html#enquire">Plan My Journey</a></div>';
  const yt = u => { const r = u.match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([\w-]{11})/); return r && r[1]; };
  const close = () => { m.classList.remove('in'); frame.innerHTML = ''; document.body.classList.remove('no-scroll'); setTimeout(() => m.hidden = true, 200); };
  document.querySelectorAll('[data-video]').forEach(b => b.addEventListener('click', () => {
    const u = b.dataset.video, id = yt(u);
    if (id) frame.innerHTML = '<iframe src="https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Sanchari video"></iframe>';
    else if (u) {
      frame.innerHTML = '<video controls autoplay playsinline src="' + u + '"></video>';
      frame.querySelector('video').addEventListener('error', () => { frame.innerHTML = soon; });
    } else frame.innerHTML = soon;
    m.hidden = false; document.body.classList.add('no-scroll'); requestAnimationFrame(() => m.classList.add('in'));
    m.querySelector('.vm-x').focus();
  }));
  m.querySelectorAll('[data-vclose]').forEach(b => b.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !m.hidden) close(); });
})();

/* Home: temple journeys expanding panels */
(function () {
  const acc = document.getElementById('templeAcc'); if (!acc) return;
  const ps = [...acc.querySelectorAll('.ta-panel')];
  const open = p => ps.forEach(x => { const on = x === p; x.classList.toggle('on', on); x.setAttribute('aria-expanded', on); });
  ps.forEach(p => {
    p.addEventListener('mouseenter', () => { if (window.matchMedia('(hover:hover)').matches) open(p); });
    p.addEventListener('click', e => { if (!p.classList.contains('on')) { e.preventDefault(); open(p); } });
    p.addEventListener('focus', () => open(p));
    p.addEventListener('keydown', e => {
      const i = ps.indexOf(p);
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); ps[(i + 1) % ps.length].focus(); }
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); ps[(i - 1 + ps.length) % ps.length].focus(); }
      if (e.key === 'Enter') { const a = p.querySelector('.ta-btn'); if (a) a.click(); }
    });
  });
})();

/* Home hero slider: fade + Ken Burns, 5s autoplay, pause on hover/interaction */
(function () {
  const root = document.getElementById('heroSlider'); if (!root) return;
  const slides = [...root.querySelectorAll('.hv-slide')], dots = [...root.querySelectorAll('.hv-dots button')];
  const DUR = 5000; let i = 0, timer = null, hover = false;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const go = n => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => { const on = k === i; s.classList.toggle('on', on); s.setAttribute('aria-hidden', !on);
      s.querySelectorAll('a').forEach(a => a.tabIndex = on ? 0 : -1);
      if (on) { const bg = s.querySelector('.hv-bg'); bg.style.animation = 'none'; void bg.offsetWidth; bg.style.animation = ''; } });
    dots.forEach((d, k) => { d.classList.toggle('on', k === i); d.setAttribute('aria-current', k === i); });
    schedule();
  };
  const schedule = () => { clearTimeout(timer); if (!hover && !reduce) timer = setTimeout(() => go(i + 1), DUR); };
  root.querySelector('.hv-arrow.prev').addEventListener('click', () => go(i - 1));
  root.querySelector('.hv-arrow.next').addEventListener('click', () => go(i + 1));
  dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
  root.addEventListener('mouseenter', () => { hover = true; clearTimeout(timer); });
  root.addEventListener('mouseleave', () => { hover = false; schedule(); });
  root.addEventListener('keydown', e => { if (e.key === 'ArrowRight') go(i + 1); if (e.key === 'ArrowLeft') go(i - 1); });
  let x0 = null;
  root.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  root.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1)); x0 = null; });
  document.addEventListener('visibilitychange', () => { if (document.hidden) clearTimeout(timer); else schedule(); });
  go(0);
})();

/* Home: temple journeys map */
(function () {
  const root = document.getElementById('templeMap'); if (!root) return;
  const pins = [...root.querySelectorAll('.tm-pin')], cards = [...root.querySelectorAll('.tm-card')],
        tabs = [...document.querySelectorAll('.tm-tab')];
  const show = i => {
    [pins, cards, tabs].forEach(list => list.forEach(el => el.classList.toggle('on', +el.dataset.i === i)));
    cards.forEach(c => { const on = +c.dataset.i === i; c.setAttribute('aria-hidden', !on); c.querySelectorAll('a').forEach(a => a.tabIndex = on ? 0 : -1); });
    tabs.forEach(t => t.setAttribute('aria-selected', +t.dataset.i === i));
  };
  [...pins, ...tabs].forEach(b => b.addEventListener('click', () => show(+b.dataset.i)));
  pins.forEach(p => p.addEventListener('mouseenter', () => { if (window.matchMedia('(hover:hover)').matches) show(+p.dataset.i); }));
  show(0);
})();

/* Home: Temple Journeys region filter */
(function () {
  const grid = document.getElementById('templeBento'); if (!grid) return;
  const pills = [...document.querySelectorAll('.tb-pill')], tiles = [...grid.querySelectorAll('.tb-tile')];
  pills.forEach(p => p.addEventListener('click', () => {
    const z = p.dataset.z;
    pills.forEach(x => { x.classList.toggle('on', x === p); x.setAttribute('aria-pressed', x === p); });
    grid.classList.toggle('filtered', z !== 'all');
    tiles.forEach(t => {
      const show = z === 'all' || t.dataset.zone === z || t.dataset.zone === 'all';
      t.hidden = !show;
      if (show) { t.style.animation = 'none'; void t.offsetWidth; t.style.animation = ''; }
    });
  }));
  pills.forEach(x => x.setAttribute('aria-pressed', x.classList.contains('on')));
})();

/* Card image sliders (Home: Adventure Journeys) */
document.querySelectorAll('[data-slider]').forEach(sl => {
  const track = sl.querySelector('.ex-track'), slides = [...track.children];
  const dots = [...sl.querySelectorAll('.ex-dots button')], count = sl.querySelector('.ex-count b');
  const prev = sl.querySelector('.ex-nav.prev'), next = sl.querySelector('.ex-nav.next');
  const idx = () => Math.round(track.scrollLeft / track.clientWidth);
  const go = i => track.scrollTo({ left: Math.max(0, Math.min(slides.length - 1, i)) * track.clientWidth, behavior: 'smooth' });
  const update = () => { const i = idx(); dots.forEach((d, k) => d.classList.toggle('on', k === i)); if (count) count.textContent = i + 1;
    if (prev) prev.disabled = i === 0; if (next) next.disabled = i === slides.length - 1; };
  prev && prev.addEventListener('click', () => go(idx() - 1));
  next && next.addEventListener('click', () => go(idx() + 1));
  dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
  let t; track.addEventListener('scroll', () => { clearTimeout(t); t = setTimeout(update, 60); });
  update();
});

/* Invoice page: build the invoice from the booking details in the URL */
(function () {
  const root = document.getElementById('invoice'); if (!root) return;
  const D = JSON.parse(document.getElementById('ivData').textContent), $i = id => document.getElementById(id);
  const q = new URLSearchParams(location.search);
  const sample = !q.get('tour') || !D.tours[q.get('tour')];
  const slug = sample ? Object.keys(D.tours)[0] : q.get('tour'), t = D.tours[slug];
  const a = Math.max(1, +q.get('a') || (sample ? 2 : 1)), c = Math.max(0, +q.get('c') || 0);
  const inr = n => '₹' + Math.round(n).toLocaleString('en-IN');
  const fmt = d => d.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
  // invoice number + booking ref: kept stable for this booking in this browser
  let inv = q.get('inv');
  if (!inv) { const n = new Date(); inv = 'SAN-' + n.getFullYear() + String(n.getMonth() + 1).padStart(2, '0') + String(n.getDate()).padStart(2, '0') + '-' + Math.floor(1000 + Math.random() * 9000);
    q.set('inv', inv); try { history.replaceState(null, '', location.pathname + '?' + q.toString()); } catch (e) {} }
  const today = new Date();
  $i('ivNo').textContent = sample ? 'SAMPLE-0001' : inv;
  $i('ivRef').textContent = sample ? 'SAMPLE' : 'BK-' + inv.split('-').pop();
  $i('ivDate').textContent = fmt(today);
  $i('ivName').textContent = q.get('name') || (sample ? 'Sample Traveller' : '—');
  $i('ivPhone').textContent = q.get('phone') || (sample ? '+91 00000 00000' : '');
  $i('ivEmail').textContent = q.get('email') || '';
  $i('ivTour').textContent = t.title; $i('ivRoute').textContent = t.route + ' · ' + t.region; $i('ivCat').textContent = t.cat;
  const start = q.get('date') ? new Date(q.get('date') + 'T00:00:00') : null;
  if (start && !isNaN(start)) { const end = new Date(start); end.setDate(end.getDate() + t.days - 1);
    $i('ivDates').textContent = fmt(start) + ' – ' + fmt(end) + ' (' + t.days + 'D / ' + t.nights + 'N)'; }
  else $i('ivDates').textContent = 'Dates to be confirmed (' + t.days + 'D / ' + t.nights + 'N)';
  const style = q.get('style') === 'individual' ? 'Individual / family' : 'Group departure';
  $i('ivStyle').textContent = style;
  $i('ivPax').textContent = a + (a > 1 ? ' adults' : ' adult') + (c ? ', ' + c + (c > 1 ? ' children' : ' child') : '');
  const rows = [[t.short + ' — tour package (adult)', a, t.price]]; if (c) rows.push([t.short + ' — tour package (child)', c, t.price]);
  $i('ivRows').innerHTML = rows.map(r => '<tr><td><b>' + r[0] + '</b><small>' + style + ' · ' + t.days + ' days / ' + t.nights + ' nights</small></td><td class="num">' + r[1] + '</td><td class="num">' + inr(r[2]) + '</td><td class="num">' + inr(r[1] * r[2]) + '</td></tr>').join('');
  $i('ivIncl').innerHTML = t.incl.map(x => '<li>' + x + '</li>').join('');
  const sub = rows.reduce((s, r) => s + r[1] * r[2], 0), tax = sub * D.tax.rate, total = sub + tax;
  $i('ivSub').textContent = inr(sub); $i('ivTaxL').textContent = D.tax.label + ' (' + Math.round(D.tax.rate * 100) + '%)';
  $i('ivTax').textContent = inr(tax); $i('ivTotal').textContent = inr(total); $i('ivDue').textContent = inr(total);
  // amount in words (Indian numbering)
  const ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
  const tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];
  const two = n => n < 20 ? ones[n] : tens[Math.floor(n / 10)] + (n % 10 ? ' ' + ones[n % 10] : '');
  const three = n => (n >= 100 ? ones[Math.floor(n / 100)] + ' Hundred' + (n % 100 ? ' ' : '') : '') + (n % 100 ? two(n % 100) : '');
  const words = n => { if (!n) return 'Zero'; const p = []; const cr = Math.floor(n / 1e7), l = Math.floor(n / 1e5) % 100, th = Math.floor(n / 1e3) % 100, r = n % 1000;
    if (cr) p.push(words(cr) + ' Crore'); if (l) p.push(two(l) + ' Lakh'); if (th) p.push(two(th) + ' Thousand'); if (r) p.push(three(r)); return p.join(' '); };
  $i('ivWords').innerHTML = '<b>Amount in words:</b> Rupees ' + words(Math.round(total)) + ' only';
  if (sample) { root.classList.add('is-sample'); $i('ivIntro').textContent = 'This is a sample invoice. Book a tour to see your own invoice here.'; }
  document.title = (sample ? 'Sample invoice' : 'Invoice ' + inv) + ' | Sanchari Travel';
  $i('ivPrint').addEventListener('click', () => window.print());
})();

/* My Account page */
(function () {
  const app = document.getElementById('acApp'); if (!app) return;
  const D = JSON.parse(document.getElementById('acData').textContent), $i = id => document.getElementById(id);
  const u = SAN.user();
  if (!u) { $i('acGuest').hidden = false; return; }
  app.hidden = false;
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const inr = n => '₹' + Math.round(n).toLocaleString('en-IN');
  const fmt = d => d.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const paint = () => {
    const me = SAN.user() || {};
    $i('acName').textContent = me.name || 'Traveller'; $i('acFirst').textContent = SAN.first(me);
    $i('acMail').textContent = me.email || me.phone || '';
    $i('acAv').textContent = (me.name || 'S').trim().split(/\s+/).map(w => w[0]).slice(0, 2).join('').toUpperCase();
  };
  paint();
  // bookings
  const bk = SAN.bookings().filter(b => D.tours[b.tour]).map(b => {
    const t = D.tours[b.tour], start = b.date ? new Date(b.date + 'T00:00:00') : null, end = start ? new Date(start) : null;
    if (end) end.setDate(end.getDate() + t.days - 1);
    const sub = t.price * ((+b.a || 1) + (+b.c || 0));
    return Object.assign({}, b, { t, start, end, total: sub * (1 + D.tax.rate), upcoming: !start || end >= today });
  });
  const invUrl = b => 'invoice.html?' + new URLSearchParams({ tour: b.tour, date: b.date || '', a: b.a, c: b.c, style: b.style, name: b.name || '', phone: b.phone || '', email: b.email || '', inv: b.inv }).toString();
  const pic = t => '<img src="' + esc(t.img) + '" alt="" data-real-js="' + esc(t.real) + '">';
  const bcard = b => '<article class="ac-bk">' + '<a class="ac-bk-img" href="' + b.tour + '.html">' + pic(b.t) + '</a>' +
    '<div class="ac-bk-body"><div class="ac-bk-top"><span class="ac-pill ' + (b.upcoming ? 'up' : 'past') + '">' + (b.upcoming ? 'Pending confirmation' : 'Completed') + '</span><small>Ref ' + esc(b.inv) + '</small></div>' +
    '<h3><a href="' + b.tour + '.html">' + esc(b.t.short) + '</a></h3>' +
    '<p class="ac-bk-meta"><span>' + (b.start ? fmt(b.start) + ' – ' + fmt(b.end) : 'Dates to be confirmed') + '</span><span>' + b.a + (b.a > 1 ? ' adults' : ' adult') + (+b.c ? ', ' + b.c + (b.c > 1 ? ' children' : ' child') : '') + '</span><span>' + (b.style === 'individual' ? 'Individual / family' : 'Group departure') + '</span></p>' +
    '<div class="ac-bk-foot"><div><small>Total (incl. ' + esc(D.tax.label) + ')</small><b>' + inr(b.total) + '</b></div><div class="ac-bk-acts">' +
    '<a class="btn btn-line" href="' + invUrl(b) + '">View invoice</a>' +
    '<a class="btn btn-gold" target="_blank" rel="noopener" href="https://wa.me/' + D.wa + '?text=' + encodeURIComponent('Hi Sanchari, about my booking ' + b.inv + ' (' + b.t.short + ').') + '">Ask on WhatsApp</a></div></div></div></article>';
  const empty = (t, p, href, cta) => '<div class="ac-empty"><b>' + t + '</b><p>' + p + '</p><a class="btn btn-gold" href="' + href + '">' + cta + '</a></div>';
  let bf = 'all';
  const drawBookings = () => {
    const list = bk.filter(b => bf === 'all' || (bf === 'upcoming' ? b.upcoming : !b.upcoming));
    $i('acBookings').innerHTML = list.length ? list.map(bcard).join('') : empty(bk.length ? 'No ' + bf + ' bookings' : 'No bookings yet', 'When you book a tour, it will appear here with its invoice.', 'temple-tours.html', 'Explore tours');
    swapImgs($i('acBookings'));
  };
  document.querySelectorAll('[data-bf]').forEach(b => b.addEventListener('click', () => { bf = b.dataset.bf; document.querySelectorAll('[data-bf]').forEach(x => x.classList.toggle('on', x === b)); drawBookings(); }));
  // wishlist
  const wcard = s => { const t = D.tours[s]; return '<article class="ac-w"><a href="' + s + '.html" class="ac-w-img">' + pic(t) + '<span>' + t.days + 'D / ' + t.nights + 'N</span></a>' +
    '<div class="ac-w-body"><small>' + esc(t.region) + ' · ' + esc(t.cat) + '</small><h3><a href="' + s + '.html">' + esc(t.short) + '</a></h3><p>' + esc(t.route) + '</p>' +
    '<div class="ac-w-foot"><b>' + inr(t.price) + '<small> / person</small></b><button type="button" class="ac-rm" data-rm="' + s + '" aria-label="Remove ' + esc(t.short) + ' from wishlist">Remove</button></div></div></article>'; };
  const drawWish = () => {
    const w = SAN.wishlist().filter(s => D.tours[s]);
    $i('acWish').innerHTML = w.length ? w.map(wcard).join('') : empty('Your wishlist is empty', 'Tap the heart on any tour or Popular journeys card to save it here.', 'index.html', 'Browse journeys');
    $i('acMiniWish').innerHTML = w.length ? w.slice(0, 3).map(s => '<a href="' + s + '.html">' + pic(D.tours[s]) + '<span><b>' + esc(D.tours[s].short) + '</b><small>From ' + inr(D.tours[s].price) + '</small></span></a>').join('') : '<p class="ac-muted">No saved tours yet.</p>';
    $i('acWish').querySelectorAll('[data-rm]').forEach(b => b.addEventListener('click', () => { SAN.toggleWish(b.dataset.rm); drawWish(); stats(); }));
    swapImgs($i('acWish')); swapImgs($i('acMiniWish'));
  };
  const stats = () => {
    const w = SAN.wishlist().filter(s => D.tours[s]).length, up = bk.filter(b => b.upcoming).length;
    document.querySelector('[data-stat="bookings"]').textContent = bk.length;
    document.querySelector('[data-stat="upcoming"]').textContent = up;
    document.querySelector('[data-stat="wishlist"]').textContent = w;
    const c = { bookings: bk.length, wishlist: w };
    document.querySelectorAll('[data-count]').forEach(el => { const n = c[el.dataset.count]; el.textContent = n ? n : ''; });
  };
  const next = bk.filter(b => b.upcoming).sort((x, y) => (x.start || 9e15) - (y.start || 9e15))[0];
  $i('acNext').innerHTML = next ? bcard(next) : empty('No upcoming trips', 'Plan your next temple, adventure or wellness journey.', 'temple-tours.html', 'Find a journey');
  swapImgs($i('acNext'));
  function swapImgs(root) { root.querySelectorAll('img[data-real-js]').forEach(im => { const u = im.dataset.realJs; if (!u) return; const t = new Image(); t.onload = () => { im.src = u; }; t.src = u; }); }
  drawBookings(); drawWish(); stats();
  // profile
  const pf = $i('acProfile'), me = SAN.user() || {};
  $i('pName').value = me.name || ''; $i('pPhone').value = me.phone || ''; $i('pEmail').value = me.email || ''; $i('pCity').value = me.city || ''; $i('pNotes').value = me.notes || '';
  pf.addEventListener('submit', e => {
    e.preventDefault();
    if (!$i('pName').value.trim()) { $i('pSaved').textContent = 'Please enter your name.'; $i('pName').focus(); return; }
    SAN.setUser({ name: $i('pName').value.trim(), phone: $i('pPhone').value.trim(), email: $i('pEmail').value.trim(), city: $i('pCity').value.trim(), notes: $i('pNotes').value.trim() });
    paint(); $i('pSaved').textContent = 'Saved'; setTimeout(() => $i('pSaved').textContent = '', 2500);
  });
  // tabs via hash
  const panes = [...document.querySelectorAll('.ac-pane')], links = [...document.querySelectorAll('.ac-link[data-pane]')];
  const go = k => { if (!panes.some(p => p.dataset.pane === k)) k = 'dashboard';
    panes.forEach(p => p.hidden = p.dataset.pane !== k); links.forEach(l => { const on = l.dataset.pane === k; l.classList.toggle('on', on); if (on) l.setAttribute('aria-current', 'page'); else l.removeAttribute('aria-current'); }); };
  window.addEventListener('hashchange', () => { go(location.hash.slice(1)); window.scrollTo({ top: 0, behavior: 'smooth' }); });
  go(location.hash.slice(1));
  $i('acLogout').addEventListener('click', () => { SAN.logout(); location.href = 'index.html'; });
})();

/* Home: popular destinations carousel - arrows, autoplay (3s, loops), pause on hover/focus */
(function () {
  const track = document.getElementById('dxTrack'); if (!track) return;
  const cards = [...track.children];
  const step = () => cards[0].getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 24);
  const atEnd = () => track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
  const go = d => {
    if (d > 0 && atEnd()) track.scrollTo({ left: 0, behavior: 'smooth' });
    else if (d < 0 && track.scrollLeft <= 4) track.scrollTo({ left: track.scrollWidth, behavior: 'smooth' });
    else track.scrollBy({ left: d * step(), behavior: 'smooth' });
  };
  document.querySelectorAll('.dx-arrow').forEach(b => b.addEventListener('click', () => { go(+b.dataset.d); restart(); }));
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let timer = null, hold = false;
  const restart = () => { clearInterval(timer); if (!reduce && !hold) timer = setInterval(() => go(1), 3000); };
  ['mouseenter', 'focusin', 'touchstart'].forEach(ev => track.addEventListener(ev, () => { hold = true; clearInterval(timer); }, { passive: true }));
  ['mouseleave', 'focusout'].forEach(ev => track.addEventListener(ev, () => { hold = false; restart(); }));
  track.addEventListener('touchend', () => { setTimeout(() => { hold = false; restart(); }, 4000); }, { passive: true });
  document.addEventListener('visibilitychange', () => { if (document.hidden) clearInterval(timer); else restart(); });
  restart();
})();

/* Plan your journey: "General enquiry" shows only name, phone, email and message */
(function(){
  document.querySelectorAll('.pj-form').forEach(function(f){
    var radios = f.querySelectorAll('input[name="pjType"]');
    if(!radios.length) return;
    var email = f.querySelector('#pjEmail'), msg = f.querySelector('#pjMsg'), title = f.querySelector('#pjTitle');
    var ph = msg ? msg.getAttribute('placeholder') : '';
    function sync(){
      var c = f.querySelector('input[name="pjType"]:checked');
      var gen = !!c && c.value === 'general';
      f.classList.toggle('is-general', gen);
      if(email) email.required = gen;
      if(msg){ msg.required = gen; msg.placeholder = gen ? msg.getAttribute('data-ph-gen') : ph; msg.rows = gen ? 5 : 3; }
      if(title) title.textContent = title.getAttribute(gen ? 'data-gen' : 'data-trip');
    }
    radios.forEach(function(r){ r.addEventListener('change', sync); });
    var want = new URLSearchParams(location.search).get('type');
    if(want){ var r0 = f.querySelector('input[name="pjType"][value="'+want.replace(/[^a-z]/g,'')+'"]'); if(r0) r0.checked = true; }
    sync();
  });
})();

/* Custom Tour Packages: autoplay (muted) video with a sound toggle; photo shows if the video can't load */
(function(){
  document.querySelectorAll('.cs-player').forEach(function(box){
    var v = box.querySelector('.cs-vid'), btn = box.querySelector('.cs-sound');
    if(!v) return;
    var fail = function(){ v.classList.add('is-off'); if(btn) btn.classList.add('is-off'); var x = box.querySelector('.cs-pp'); if(x) x.classList.add('is-off'); };
    var srcs = v.querySelectorAll('source'); if(srcs.length) srcs[srcs.length-1].addEventListener('error', fail);
    v.addEventListener('error', fail);
    v.muted = true;
    var p = v.play(); if(p && p.catch) p.catch(function(){});
    var pp = box.querySelector('.cs-pp'), userPaused = false;
    var syncPP = function(){ if(!pp) return; var paused = v.paused; pp.setAttribute('aria-pressed', String(paused)); pp.setAttribute('aria-label', paused ? 'Play video' : 'Pause video'); };
    v.addEventListener('play', syncPP); v.addEventListener('pause', syncPP);
    if(pp) pp.addEventListener('click', function(){
      if(v.paused){ userPaused = false; var q = v.play(); if(q && q.catch) q.catch(function(){}); }
      else { userPaused = true; v.pause(); }
    });
    if(btn) btn.addEventListener('click', function(){
      v.muted = !v.muted;
      if(!v.muted){ var q = v.play(); if(q && q.catch) q.catch(function(){}); }
      btn.setAttribute('aria-pressed', String(!v.muted));
      btn.setAttribute('aria-label', v.muted ? 'Turn sound on' : 'Turn sound off');
    });
    if('IntersectionObserver' in window){
      new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ if(!userPaused){ var r=v.play(); if(r&&r.catch) r.catch(function(){}); } } else if(!v.paused){ v.pause(); } }); }, {threshold:.15}).observe(v);
    }
  });
})();
