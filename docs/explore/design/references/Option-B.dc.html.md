<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Projects — Option B Dark band</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
body{margin:0;background:#f5f5f4;color:#0f172a;font-family:Inter,system-ui,sans-serif}
.hero{background:#0f172a;color:#f8fafc}
.hero-in{max-width:1200px;margin:0 auto;padding:64px 32px 56px;box-sizing:border-box}
h1{margin:0;font-size:48px;line-height:56px;font-weight:600;letter-spacing:-0.025em}
.intro{margin:16px 0 0;font-size:18px;line-height:28px;color:#cbd5e1;max-width:640px}
.proof{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:40px 0 0;padding:0;list-style:none}
.proof li{position:relative;background:#111c33;border:1px solid #1e293b;border-radius:16px;padding:28px 28px 24px;overflow:hidden}
.proof li::before{content:"";position:absolute;left:0;top:0;right:0;height:4px;background:#60a5fa}
.proof strong{display:block;font-size:56px;line-height:56px;font-weight:700;letter-spacing:-0.03em;color:#f8fafc}
.proof span{display:block;margin-top:12px;font-size:15px;line-height:22px;color:#cbd5e1}
.proof em{display:block;margin-top:6px;font-style:normal;font-size:14px;line-height:20px;color:#93c5fd}
.wrap{max-width:1200px;margin:0 auto;padding:56px 32px 72px;box-sizing:border-box}
.section-title{margin:0 0 24px;font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.section-title + .section-title,.section-gap{margin-top:56px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin:0;padding:0;list-style:none}
.grid--featured{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.card{position:relative;display:flex;flex-direction:column;gap:12px;background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:28px;box-shadow:0 8px 24px rgba(15,23,42,.12)}
.card--featured{padding:32px;box-shadow:0 12px 32px rgba(15,23,42,.16);border-top:4px solid #1d4ed8}
.top{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap}
.tags{display:flex;flex-wrap:wrap;gap:8px}
.sector,.tag{display:inline-block;padding:4px 10px;border-radius:999px;font-size:12px;line-height:16px;font-weight:600}
.sector{border:1px solid #93c5fd;background:#eff6ff;color:#1e40af}
.tag{border:1px solid #cbd5e1;background:#f8fafc;color:#334155}
.year{font-size:14px;line-height:20px;font-weight:500;color:#475569;padding-top:4px}
h3{margin:12px 0 0;font-size:28px;line-height:34px;font-weight:600;letter-spacing:-0.015em}
.card--featured h3{font-size:32px;line-height:38px}
h3 a{color:inherit;text-decoration:none}
h3 a::after{content:"";position:absolute;inset:0;border-radius:16px}
h3 a:hover{text-decoration:underline}
h3 a:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
.client{margin:0;font-size:14px;line-height:20px;font-weight:500;color:#334155}
.company{margin:0;font-size:13px;line-height:20px;color:#475569}
.summary{margin:auto 0 0;padding-top:14px;border-top:1px solid #e2e8f0;font-size:15px;line-height:24px;color:#334155}
.card--featured .summary{font-size:16px;line-height:26px}
.cta{margin-top:56px;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;background:#0f172a;color:#f8fafc;border-radius:16px;padding:32px}
.cta p{margin:0;font-size:18px;line-height:28px;font-weight:500}
.btn{display:inline-block;padding:12px 20px;border-radius:8px;background:#f8fafc;color:#0f172a;font-weight:600;font-size:15px;text-decoration:none}
@media (max-width:1023px){.grid--featured{grid-template-columns:minmax(0,1fr)}}
@media (max-width:767px){.hero-in{padding:44px 16px 40px}h1{font-size:36px;line-height:44px}.proof{grid-template-columns:minmax(0,1fr)}.proof strong{font-size:48px;line-height:48px}.wrap{padding:40px 16px 48px}.grid{grid-template-columns:minmax(0,1fr);gap:20px}h3,.card--featured h3{font-size:24px;line-height:30px}.card--featured{padding:24px}}
</style>
</helmet>
<header class="hero">
  <div class="hero-in">
    <h1>Projects</h1>
    <p class="intro">I love making projects succeed, using both Agile and Waterfall across different markets.</p>
    <ul class="proof">
      <li><strong>15+</strong><span>years leading software and infrastructure delivery</span></li>
      <li><strong>5</strong><span>industries</span></li>
      <li><strong>10+</strong><span>projects, from on-site rollouts to cloud migrations</span></li>
    </ul>
  </div>
</header>

<main class="wrap">
  <h2 class="section-title">Featured projects</h2>
  <ul class="grid grid--featured">
    <li><article class="card card--featured">
      <div class="top"><div class="tags"><span class="sector">Capital Markets</span><span class="tag">C#</span><span class="tag">Agile</span><span class="tag">Presales</span></div><span class="year">2021–2025</span></div>
      <h3><a href="#">Cloud integration and process refactoring</a></h3>
      <p class="client">Client: DFA</p>
      <p class="company">Endava · Agile Project Manager</p>
      <p class="summary">Led Agile delivery of an API Gateway and the refactoring of about 60 business processes during a move to Azure.</p>
    </article></li>
    <li><article class="card card--featured">
      <div class="top"><div class="tags"><span class="sector">Pharmaceutical</span><span class="tag">SAP</span><span class="tag">e-Invoicing</span><span class="tag">3rd Party</span><span class="tag">Waterfall</span></div><span class="year">2017–2018</span></div>
      <h3><a href="#">Order-to-Cash for SAP migration</a></h3>
      <p class="client">Client: GSK</p>
      <p class="company">TCS · e-Invoicing - Order to Cash (O2C) Stream Lead</p>
      <p class="summary">Led the Order-to-Cash workstream, including e-invoicing integrations, across four countries in GSK's SAP migration.</p>
    </article></li>
    <li><article class="card card--featured">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Presales</span><span class="tag">Waterfall</span></div><span class="year">2014</span></div>
      <h3><a href="#">VAS delivery for 4G market expansion</a></h3>
      <p class="client">Client: Entel Peru</p>
      <p class="company">Comverse · Senior Project Lead — Presales Support / On-site Implementation Lead</p>
      <p class="summary">Led on-site implementation of value-added services for Entel's entry into Peru and its new 4G network.</p>
    </article></li>
  </ul>

  <h2 class="section-title section-gap">More projects</h2>
  <ul class="grid">
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Media</span><span class="tag">GCP</span><span class="tag">DevOps</span><span class="tag">Agile</span></div><span class="year">2025–2026</span></div>
      <h3><a href="#">Greenfield Web and Mobile platform delivery</a></h3>
      <p class="client">Client: DCTX</p>
      <p class="company">Endava · Scrum Master</p>
      <p class="summary">Led the web, mobile, back-end, data migration, and DevOps teams for a new sports media platform on GCP.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Aviation</span><span class="tag">Azure</span><span class="tag">Oracle</span><span class="tag">Data warehouse</span><span class="tag">Agile</span></div><span class="year">2021</span></div>
      <h3><a href="#">Azure data warehouse migration definition</a></h3>
      <p class="client">Client: Avianca</p>
      <p class="company">TCS · Technical Project Manager / Client Partner</p>
      <p class="summary">Developed the business case, TCO model, and migration roadmap to move a data warehouse from on-premises Oracle to Azure.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Big Data</span><span class="tag">SOX</span><span class="tag">Agile</span></div><span class="year">2018–2019</span></div>
      <h3><a href="#">SOX control using Big Data</a></h3>
      <p class="client">Client: Tigo</p>
      <p class="company">TCS · Project / Program Delivery Lead</p>
      <p class="summary">Led delivery of a Big Data platform to automate about 25 SOX control processes, with teams in Colombia and India.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Project recovery</span><span class="tag">Waterfall</span></div><span class="year">2015</span></div>
      <h3><a href="#">Project recovery and customer confidence</a></h3>
      <p class="client">Client: Entel Chile</p>
      <p class="company">Comverse · Senior Project Lead — Project Recovery / On-site Delivery Lead</p>
      <p class="summary">Recovered a delayed project by rebuilding a credible delivery plan, then took the solution to production go-live.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Waterfall</span></div><span class="year">2013</span></div>
      <h3><a href="#">VAS platform upgrade for 4G</a></h3>
      <p class="client">Client: Claro Peru</p>
      <p class="company">Comverse · Senior Project Lead — On-site Implementation / Project Lead</p>
      <p class="summary">Coordinated the value-added services platform upgrade and its integration with Claro's new 4G network.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Prepaid charging</span><span class="tag">Waterfall</span></div><span class="year">2012</span></div>
      <h3><a href="#">VAS platform implementation</a></h3>
      <p class="client">Client: GT&amp;T Guyana</p>
      <p class="company">Comverse · Senior Project Lead — On-site Implementation</p>
      <p class="summary">Led on-site implementation of a new value-added services platform, integrated with existing prepaid charging systems.</p>
    </article></li>
    <li><article class="card">
      <div class="top"><div class="tags"><span class="sector">Telecommunications</span><span class="tag">Relocation</span><span class="tag">Waterfall</span></div><span class="year">2011–2012</span></div>
      <h3><a href="#">VAS platform relocation</a></h3>
      <p class="client">Client: Digicel Jamaica</p>
      <p class="company">Comverse · Senior Project Lead — Implementation Lead / Customer Delivery Lead</p>
      <p class="summary">Led the on-site relocation of a critical value-added services platform to Jamaica after the Haiti earthquake.</p>
    </article></li>
  </ul>

  <div class="cta">
    <p>Let's talk about your next delivery challenge.</p>
    <a class="btn" href="#">Contact me</a>
  </div>
</main>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1280,"height":2300}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
