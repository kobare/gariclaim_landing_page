import os
from pathlib import Path
from datetime import date, timedelta

POSTS = [
    # ---- 1 ----
    {
        "date": "2025-01-15", "category": "Operations",
        "slug": "how-to-set-up-job-cards-in-your-garage",
        "title": "How to Set Up a Job Card System in Your Garage",
        "description": "A practical guide to designing and implementing job cards for a Kenyan auto repair workshop, from vehicle intake to release.",
        "keywords": "job card system for garage Kenya, garage job card template, workshop job tracking",
        "body": """
Every garage in Kenya has a story about a job that went wrong because of paperwork. A part that was ordered twice. A customer who was told one price and charged another. A vehicle that sat idle for three days because nobody remembered whose bay it was in.

A job card fixes all of that, if you set it up right.

## What a job card actually does

A job card is not a receipt. It is a contract between your garage and a specific vehicle for a specific piece of work. It should record:

- Vehicle identification: plate, VIN, make, model, mileage at intake
- Customer details: name, phone, who authorised the work
- Problem description: what the customer reported
- Diagnosis: what your technician found
- Work authorised: parts and labour, with prices
- Technician assignment: who is responsible for what
- Status: pending, in progress, awaiting parts, QC, ready for release
- Parts used: pulled from inventory and logged
- Photos: before and after
- Sign-offs: customer, QC technician, and release authorisation

## The four-stage flow that works for most Kenyan garages

1. Intake. Vehicle arrives, front desk opens the job card, captures photos, logs mileage.
2. Diagnosis and quotation. Technician inspects, lists work, front desk prices it and gets approval.
3. Repair. Parts are pulled, labour logged, status updated as work progresses.
4. QC and release. Final inspection, signed satisfaction note, release letter, invoice.

Most problems in Kenyan garages happen between stage 2 and stage 3, where the verbal approval the customer gave isn't quite what the technician understood.

## The signed approval letter

The single most valuable process change is to have every job authorised in writing before any technician starts work. A printed or digital authorisation letter, signed by the customer or the insurer, uploaded against the job card, closes 80 percent of disputes before they start.

With Gariclaim, authorisation letters are uploaded and protected behind OTP verification so the price the customer agreed to is the price on the final invoice.

## Why paper job cards fail

Paper job cards work for garages doing three to five jobs a week. Past 10 jobs a week, four things break:

- Cards get lost between the front desk and the workshop floor
- Parts get pulled without being logged against the job
- Nobody can see the current status of every vehicle at a glance
- Invoicing lags days behind completion

Digital job cards fix all four at once. The moment a part is pulled, it hits the job card and the inventory count updates.

## Getting started

If you are moving from paper, do not try to digitise everything at once. Start with intake and vehicle records, then job card creation and status, then parts pulled against job cards, then invoicing from completed job cards.

Once those four are running, extend the same flow to insurance repairs, add QC and release sign-offs, then roll out payroll for your staff.

[Start a free Gariclaim trial](https://garage.gariclaim.co.ke) and set up your first digital job card in under an hour.
"""
    },
    # ---- 2 ----
    {
        "date": "2025-01-22", "category": "Tax & Compliance",
        "slug": "vat-compliance-for-kenyan-garages",
        "title": "VAT Compliance for Kenyan Garages: A Practical Guide",
        "description": "What every garage owner in Kenya needs to know about VAT registration, invoicing, and filing with KRA, plus common mistakes that trigger audits.",
        "keywords": "VAT compliance Kenya garage, KRA VAT filing, garage VAT return",
        "body": """
If your garage has crossed KES 5 million in annual turnover, VAT registration with KRA is not optional. And for many garage owners, the process feels like a maze of acronyms: VAT3, iTax, input tax, output tax, PIN certificates.

This guide cuts through it.

## When you must register for VAT

KRA requires VAT registration when your taxable turnover hits KES 5,000,000 in any 12-month period. Once registered, you must:

- Charge 16 percent VAT on all taxable supplies
- File VAT returns (Form VAT3) by the 20th of the following month
- Remit the net VAT due to KRA by the same deadline

If you are below the threshold, you can still register voluntarily. This is often useful if your main customers are VAT-registered businesses who want to claim input tax.

## What counts as taxable for a garage

- Repairs and labour, standard-rated at 16 percent
- Parts sold over the counter, standard-rated at 16 percent
- Oil and consumables, standard-rated at 16 percent
- Insurance claim work, where the VAT treatment depends on how the invoice is structured

The insurance case is the one that trips up most garages. If the insurer pays you directly for the repair, that payment is still your taxable supply and you must remit the VAT.

## Input VAT: what you can claim

Every part, tool, or service you buy from a VAT-registered supplier comes with input VAT you can offset against your output VAT. To claim it, you must hold:

- A valid ETR receipt or tax invoice showing the supplier's PIN
- Proof the purchase was for the business

Disallowed input VAT includes fuel, entertainment, and personal expenses. Garage owners get caught claiming fuel constantly. Do not be one of them.

## The monthly rhythm

Here is a filing calendar that keeps most garages out of trouble:

- Days 1 to 5: reconcile the previous month's sales and purchases
- Days 6 to 10: match supplier invoices to ETR receipts
- Days 11 to 15: prepare the VAT3 return
- Days 16 to 19: review and file on iTax
- Day 20: payment deadline

Set a recurring calendar reminder for the 20th. Missing the deadline triggers automatic penalties of KES 10,000 or 5 percent of the tax due, whichever is higher.

## Common mistakes that trigger audits

Three patterns attract KRA attention faster than anything else:

1. Claiming input VAT on purchases with no valid ETR receipt
2. Filing nil returns every month while making visible sales
3. Mismatching the sales declared on VAT3 against the turnover declared for income tax

Any one of these alone can be explained. Two or more together is an audit invitation.

## How Gariclaim helps

Gariclaim ships with a Kenyan chart of accounts and calculates output and input VAT automatically on every invoice, purchase, and job card. At month end, you export a VAT summary that maps directly to Form VAT3.

Because every transaction is logged against a job card or supplier bill, when KRA asks for supporting documents, you produce them in minutes rather than days.

[Start a free trial](https://garage.gariclaim.co.ke) and run your next VAT cycle without the panic.
"""
    },
    # ---- 3 ----
    {
        "date": "2025-01-29", "category": "Insurance",
        "slug": "managing-insurance-claims-in-kenyan-garages",
        "title": "Managing Insurance Claims in a Kenyan Garage",
        "description": "How to handle insurer and assessor workflows so insurance jobs move smoothly from authorisation to payment, without disputes or delays.",
        "keywords": "insurance claims garage Kenya, assessor workflow, insurer billing garage",
        "body": """
Insurance jobs are the lifeblood of most mid-sized Kenyan garages. They also generate the most disputes, the slowest payments, and the most paperwork.

The garages that handle insurance jobs profitably all do the same four things well.

## 1. Capture the right identifiers at intake

The moment a vehicle arrives for an insurance job, capture the insurer name, policy number, claim number, assessor name and contact, the authorised repair limit, and the customer's own contact details.

Even when the insurer pays, the customer chases progress. Having their number on the job card saves a lot of back-and-forth.

Any missing identifier will slow down the eventual payout. Get them all on day one.

## 2. Do not touch the vehicle until you have written authorisation

This is the single rule that separates profitable insurance jobs from nightmares. A verbal go-ahead from an assessor is not authorisation.

You need a signed authorisation letter with the approved scope of work, the approved amounts for parts and labour, and confirmation that the claim is valid and not under investigation.

Without those in hand, you are gambling your workshop time on the insurer's eventual decision.

## 3. Handle supplements cleanly

Frequently, once the technician opens up the vehicle, more damage is discovered than the assessor saw. This is where garages lose money.

The right process:

1. Stop work the moment a supplement is needed
2. Photograph the additional damage
3. Submit a supplement quotation to the assessor in writing
4. Wait for written approval before continuing

Garages that continue work and hope the insurer will pay retroactively usually eat the cost. Gariclaim lets you raise supplement quotations directly against the job card, keep the full approval trail, and invoice only what was authorised.

## 4. Invoice fast, invoice accurately

The insurer will pay within 30 to 60 days if the invoice is clean. It will be rejected and returned if the invoice references an amount higher than the approved limit, parts listed do not match the assessment report, or the claim or policy number is missing or wrong.

Every rejected invoice adds two weeks to your payment cycle. Getting the invoice right the first time is worth more than chasing the second time.

## Tracking the pipeline

Keep a running view of every insurance job split by status: awaiting authorisation, awaiting parts, in progress, awaiting supplement approval, QC, awaiting release, invoiced and awaiting payment.

At any given moment you should know how much is owed to you by each insurer. If an insurer is consistently slow, that is a business conversation to have.

## What Gariclaim does

Gariclaim records insurer, assessor, policy and claim numbers against every job card. It tracks supplements separately from the original authorisation, prevents invoicing above approved limits, and gives you a per-insurer outstanding balance report so you know exactly who owes what.

[Start a free trial](https://garage.gariclaim.co.ke) and stop chasing insurance payments.
"""
    },
    # ---- 4 ----
    {
        "date": "2025-02-05", "category": "Growth",
        "slug": "how-to-price-auto-repair-services-in-kenya",
        "title": "How to Price Auto Repair Services in Kenya",
        "description": "A practical framework for pricing labour, parts, and diagnostics in a Kenyan garage so you stay competitive without losing money.",
        "keywords": "auto repair pricing Kenya, garage labour rates, how to price car repair",
        "body": """
Most Kenyan garages price their work by gut feel. A technician glances at the vehicle, names a number, and the customer either nods or walks away.

That is not a pricing strategy. That is gambling.

## The three components of every repair price

Every job has three cost components: parts, labour, and diagnostics. Price each separately.

Parts are the easiest. You have an invoice from your supplier and a standard markup. Most Kenyan garages run a markup of 20 to 40 percent on parts, higher on rare or imported components.

Labour is where garages get tripped up. If you do not know your hourly cost, you cannot price labour consistently.

Diagnostics is a distinct service. A 30-minute scan with a diagnostic tool is not the same as a 30-minute oil change.

## Calculating your true labour rate

Start with what a technician costs you per month: salary, statutory deductions (PAYE, SHIF, NSSF, Housing Levy), leave, and any uniform or tool allowance. Then divide by the productive hours they actually work.

Say a technician costs you KES 45,000 a month all-in and works 160 productive hours. That is KES 281 per hour. Add rent, utilities, admin, and profit. Most Kenyan garages land between KES 800 and KES 1,800 per hour for standard labour.

Post that rate. Customers respect transparency.

## Markup on parts: common traps

Do not markup parts you did not source. If the customer brings their own spare and asks you to fit it, you charge labour only, plus a small fitting fee.

Do not hide markup in the labour line. Customers eventually notice and it damages trust.

Do not discount parts to win a job. Discount the labour if you must, but leave parts at a fair margin.

## Diagnostic pricing

Diagnostics is a distinct service and should be billed separately. A full vehicle inspection with a written report is worth KES 2,000 to KES 5,000 depending on depth.

Some garages charge for diagnostics and then credit it against the repair if the customer proceeds. That is a good compromise. It discourages tyre-kickers while rewarding real customers.

## When to negotiate and when to walk

Negotiate on scope, not on price. If the customer wants to spend less, offer fewer services, not the same services at a lower rate.

If a customer pushes hard below your cost, walk away. A job you lose money on is worse than no job.

## Put prices on paper

Every quote should be a written document with an itemised parts list, labour hours, and diagnostics. Signed by the customer before work starts.

Gariclaim generates itemised quotations from your item catalogue and price lists, so every quote is consistent and every approved job is auditable.

[Start a free trial](https://garage.gariclaim.co.ke) and stop guessing on price.
"""
    },
    # ---- 5 ----
    {
        "date": "2025-02-12", "category": "Tax & Compliance",
        "slug": "kra-pin-registration-guide-for-garage-owners",
        "title": "KRA PIN Registration Guide for Garage Owners",
        "description": "Step by step guide to registering your garage for a KRA PIN, and the tax obligations that follow once you are on the system.",
        "keywords": "KRA PIN registration garage, iTax garage, KRA compliance Kenya small business",
        "body": """
Every business in Kenya that engages with KRA needs a Personal Identification Number. For garages, it unlocks everything from paying PAYE for your staff to filing your annual returns.

## What a KRA PIN actually is

A KRA PIN is an 11-character identifier that ties your business to every tax filing you make. Without it you cannot:

- Register employees for PAYE
- Register for VAT once you cross the turnover threshold
- File annual returns
- Open a business bank account
- Tender for government or corporate contracts

## Registering for a PIN

Registration happens on iTax. The process takes about 20 minutes if you have everything ready.

You will need:

- National ID or passport
- KRA PIN of any director or owner (individual)
- Business registration certificate (from eCitizen if you are a company or business name)
- Physical and postal address
- Email and phone number
- Bank account details

Once you submit, KRA typically issues the PIN within 24 to 48 hours.

## Common registration mistakes

Three mistakes catch most garage owners:

1. Registering as an individual when you are operating as a company. Fix this by registering a separate PIN for the business entity.

2. Using a residential address. Use the physical address of the garage itself. KRA sometimes verifies this.

3. Skipping the obligation check. Before you finish registration, iTax asks you to select your tax obligations: Income Tax for individuals, Corporate Tax for companies, VAT if you are above the threshold, PAYE if you have employees.

Select all that apply. You can add more later if needed, but leaving them off causes problems when you try to file.

## What happens after registration

Once you have a PIN, you are on the radar. Even if you have zero turnover, you must file a nil return every year by 30 June for individuals and by the end of the sixth month after your financial year end for companies.

Missing annual returns triggers penalties. The earlier you file, the less painful it becomes.

## PAYE for employees

If you employ anyone, you must register for PAYE and remit deductions monthly by the 9th of the following month. The deductions include PAYE tax, SHIF, NSSF, and Housing Levy.

This is where Gariclaim saves the most pain. It calculates all four deductions automatically every payroll run and generates the P10, NSSF, SHIF, and Housing Levy schedules you submit to KRA.

## Annual returns

Even if you file nothing else during the year, do not miss the annual return. It is the single filing KRA watches most closely for small businesses.

## Staying compliant without panic

The garages that never get audited are the ones that file on time, keep receipts, and reconcile their books monthly. That is the whole secret.

Gariclaim keeps a running ledger of every transaction, calculates VAT and PAYE automatically, and stores your KRA PIN against your organisation profile so nothing falls through the cracks.

[Start a free trial](https://garage.gariclaim.co.ke) and stop dreading KRA.
"""
    },
    # ---- 6 ----
    {
        "date": "2025-02-19", "category": "Inventory",
        "slug": "how-to-reduce-spare-parts-theft-in-your-workshop",
        "title": "How to Reduce Spare Parts Theft in Your Workshop",
        "description": "Practical systems to stop inventory loss in a Kenyan garage, from physical controls to digital tracking.",
        "keywords": "spare parts theft garage, reduce inventory loss workshop, stop theft in auto repair",
        "body": """
Inventory loss is the silent killer of Kenyan garages. Nobody reports it as theft because nobody can prove it. The count is just always a little lower than the records.

A 5 percent loss on KES 3 million of parts a year is KES 150,000 gone. That is a technician's annual salary.

## Why garage inventory disappears

Four patterns account for almost all loss:

1. Parts pulled for a job and never logged against the job card
2. Parts borrowed for a favour and never returned
3. Parts sold over the counter without a receipt
4. Parts damaged during fitting and quietly discarded

The first is by far the most common. It is usually not malicious. A technician pulls a part, gets busy, forgets to write it down.

## The control that matters most

The single most effective control is to require every part movement to be logged against something. A job card or a POS sale. Nothing in, nothing out, without a digital trail.

That means when a technician pulls a brake pad, either:

- It goes onto a job card, and the job card logs which vehicle and which customer
- It goes out over the counter with a printed receipt
- It stays on the shelf

No third option.

## Physical controls that support the system

Digital controls only work if the physical side is disciplined too.

- Keep the parts store locked during working hours
- One person issues parts. If everyone can help themselves, nobody is accountable
- Post the stock level on the shelf so technicians can see what they take
- Do a weekly spot check on the top 20 fastest-moving items

## Weekly cycle counts beat annual stocktakes

An annual stocktake tells you what you lost last year. A weekly cycle count on high-value items tells you what you lost this week, while you can still investigate.

Pick the top 20 parts by value. Count them every Friday. Investigate every variance above KES 1,000 that same day.

## When loss continues

If inventory still disappears after these controls are in place, the problem is cultural, not systemic. Somebody has decided the rules do not apply to them.

The conversation is uncomfortable but necessary. Bring the numbers. Show the trend. Ask directly.

## How Gariclaim helps

Gariclaim logs every part movement against a job card or POS sale. Stock levels update in real time, and the full movement history shows exactly when and by whom each part was issued.

You can filter movements by user, by date, and by job card. If a part is missing, the trail tells you where it went.

[Start a free trial](https://garage.gariclaim.co.ke) and stop the leak.
"""
    },
    # ---- 7 ----
    {
        "date": "2025-02-26", "category": "Payroll",
        "slug": "payroll-compliance-kenya-paye-shif-nssf-housing-levy",
        "title": "Payroll Compliance in Kenya: PAYE, SHIF, NSSF, and Housing Levy",
        "description": "How the four statutory deductions work in Kenya, how to calculate them, and what to file with KRA every month.",
        "keywords": "PAYE Kenya payroll, SHIF NSSF housing levy, Kenya statutory deductions",
        "body": """
If you employ anyone in Kenya, four deductions come out of every paycheck. Three go to statutory bodies, one goes to the tax authority. Getting them wrong creates penalties that compound fast.

Here is how each one works.

## PAYE (Pay As You Earn)

PAYE is income tax withheld from your employee's salary and remitted to KRA on their behalf. You are the tax collector here, not the taxpayer.

PAYE is progressive. The first KES 24,000 a month is tax-free. From there the bands step up, topping out at 30 percent for income above KES 32,333 a month, plus a 5 percent surcharge on income over KES 500,000 a year.

Every employee also gets a personal relief of KES 2,400 a month, which reduces the tax calculated.

PAYE is filed on Form P10 and remitted by the 9th of the following month.

## SHIF (Social Health Insurance Fund)

SHIF replaced NHIF in late 2024. It is calculated as 2.75 percent of gross salary, with a minimum of KES 300 a month. There is no upper cap.

SHIF is deducted from the employee and remitted to the Social Health Authority.

## NSSF (National Social Security Fund)

NSSF is a pension contribution. It has two tiers:

- Tier 1: 6 percent of pensionable pay up to the lower earnings limit
- Tier 2: 6 percent of pensionable pay between the lower and upper earnings limits

Both the employee and the employer contribute. So NSSF effectively doubles the deduction from your perspective as an employer.

## Housing Levy

The Affordable Housing Levy is 1.5 percent of gross salary, matched by the employer at another 1.5 percent. Total 3 percent of gross pay.

It was reintroduced in 2024 and remitted to KRA monthly alongside PAYE.

## The monthly rhythm

Every month, by the 9th:

- PAYE, SHIF, Housing Levy to KRA
- NSSF to NSSF
- Each employee gets a payslip

Miss the 9th and you accrue penalties. KRA charges 5 percent of the tax due plus 1 percent interest per month. NSSF charges similar.

## Common mistakes

The three mistakes we see most often in Kenyan garages:

1. Ignoring Housing Levy because "it might be repealed". It has not been. Remit it.
2. Using the old NHIF rates for SHIF. SHIF replaced it. Check your calculations.
3. Deducting NSSF from the employee but not contributing the employer share. Both halves are required.

## How Gariclaim helps

Gariclaim runs payroll daily, weekly, biweekly, or monthly. It calculates PAYE, SHIF, NSSF, and Housing Levy automatically, generates payslips for each employee, and produces the P10 and statutory schedules you submit to KRA and NSSF.

Leave management and salary advances are integrated, so deductions for advances or unpaid leave are applied correctly.

[Start a free trial](https://garage.gariclaim.co.ke) and run payroll without the spreadsheet panic.
"""
    },
    # ---- 8 ----
    {
        "date": "2025-03-05", "category": "Finance",
        "slug": "how-to-manage-mpesa-payments-in-a-kenyan-garage",
        "title": "How to Manage M-Pesa Payments in a Kenyan Garage",
        "description": "Best practices for tracking M-Pesa payments from customers, recording them against job cards, and reconciling against your till statement.",
        "keywords": "M-Pesa payments garage, M-Pesa reconciliation Kenya, record M-Pesa payment",
        "body": """
Almost every Kenyan garage takes M-Pesa. Almost none of them record it properly.

The result is a persistent gap between what the till shows and what the job cards show. At the end of the month, nobody can explain the difference.

## The three M-Pesa flows in a garage

Every garage has three M-Pesa channels running at the same time:

1. Customer payments for jobs. Usually a Buy Goods Till Number.
2. Customer payments for parts at the counter. Sometimes the same till, sometimes a separate one.
3. Payments out to suppliers. This is the Send Money channel from your business line.

Each channel needs to be tracked separately.

## Recording M-Pesa against job cards

The moment a customer pays, record the M-Pesa transaction code against the job card. Not "M-Pesa" as the payment method. The actual confirmation code.

That ten-character code is the receipt. If a customer ever claims they paid and you cannot find it, the code proves or disproves it in seconds.

In Gariclaim, M-Pesa payments are recorded as a payment against the invoice with the transaction code in the reference field. The job card immediately shows the payment status.

## Reconciling the till statement

Every month, download your M-Pesa statement from the Safaricom portal. It is a CSV file with every transaction, timestamp, code, and amount.

Match each transaction to a job card or POS sale. Anything unmatched is either:

- A payment you recorded in the system but never got (rare)
- A payment you got but never recorded (common)

Either way, the reconciliation reveals it.

## Avoid the cash-in-pocket habit

The most dangerous M-Pesa habit is accepting a customer payment into a personal M-Pesa line instead of the business till. It seems harmless. It is not.

Three things happen when personal M-Pesa is used for business:

1. You cannot prove the payment in a dispute
2. It never makes it into your books
3. KRA treats it as personal income, not business revenue

If you take payments personally, transfer everything to the business account same day and record it against the job card.

## Signatures and confirmation

For payments over KES 20,000, always take a signature on the job card acknowledging the transaction code and amount. It protects both parties.

## How Gariclaim helps

Gariclaim records M-Pesa payments against invoices and POS sales with the transaction code. At month end, you can import the Safaricom statement and reconcile it against recorded payments in the system.

Because every payment is tied to a job or a counter sale, you have a clean audit trail of where every shilling came from.

[Start a free trial](https://garage.gariclaim.co.ke) and close the gap between your till and your books.
"""
    },
    # ---- 9 ----
    {
        "date": "2025-03-12", "category": "Growth",
        "slug": "auto-repair-shop-kpis-kenyan-garage-owners-should-track",
        "title": "8 KPIs Every Kenyan Garage Owner Should Track",
        "description": "The eight numbers that tell you whether your garage is healthy, and how to calculate each one.",
        "keywords": "garage KPIs Kenya, auto repair shop metrics, workshop performance indicators",
        "body": """
You cannot improve what you do not measure. Yet most Kenyan garage owners run on feel. They know last month was busy, but not whether it was profitable.

Here are the eight numbers that tell you the truth.

## 1. Revenue per bay per day

Total revenue divided by the number of working bays divided by working days in the month.

This tells you how hard each bay is working. In a healthy Kenyan garage, this should be trending upward month on month. If it is flat, you are either undercharging or not filling the bays.

## 2. Utilisation rate

Hours a bay was in use divided by hours available.

A garage running under 60 percent utilisation has spare capacity. Above 85 percent and you are turning away work.

## 3. Average job value

Total revenue divided by the number of jobs completed.

Track this weekly. If it drops, either job scope is shrinking or you are discounting. If it rises, your upselling is working.

## 4. Technician productivity

Billed hours divided by paid hours per technician.

Most Kenyan technicians average 60 to 75 percent. Below 60 percent suggests idle time or rework. Above 85 percent for a sustained period is unsustainable and leads to burnout.

## 5. Parts margin

(Revenue from parts minus cost of parts) divided by revenue from parts.

Target: 30 to 40 percent. If it drops below 25 percent, either your supplier pricing moved or you are discounting without realising.

## 6. Days sales outstanding

Average accounts receivable divided by average daily revenue.

For garage work, this should be under 30 days for retail customers, under 60 for insurance jobs. Anything above is cash flow risk.

## 7. Rework rate

Jobs that came back for the same issue divided by total jobs.

Target: under 3 percent. Above 5 percent suggests a training or QC issue.

## 8. Customer return rate

Customers who returned within 12 months divided by total customers.

Healthy Kenyan garages see 40 to 60 percent return. If it is below 30 percent, something in the customer experience is broken.

## How to track them without spreadsheets

Most of these numbers fall out of your job cards, invoices, and inventory data automatically, if that data lives in a system.

Gariclaim's advanced reports show revenue, margin, and utilisation without you having to export anything or build a single spreadsheet formula.

[Start a free trial](https://garage.gariclaim.co.ke) and see the truth about your garage.
"""
    },
    # ---- 10 ----
    {
        "date": "2025-03-19", "category": "Operations",
        "slug": "how-to-hire-and-train-garage-technicians-in-kenya",
        "title": "How to Hire and Train Garage Technicians in Kenya",
        "description": "A practical framework for finding, vetting, and retaining good technicians in a Kenyan auto repair workshop.",
        "keywords": "hire garage technician Kenya, train auto mechanic Kenya, technician retention",
        "body": """
Your technicians are your product. Everything the customer experiences runs through their hands. Hire well and the rest is easier. Hire badly and no system will save you.

Here is what actually works in Kenya.

## Where to find technicians

Three sources produce the best hires:

1. Referrals from your existing team. They know who is good in the trade.
2. Technical colleges: Kabete National Polytechnic, Nyeri, and other TVET institutions.
3. Poaching from a competitor is not recommended. It rarely works and it damages your reputation in the trade.

## What to look for beyond skill

Skill is table stakes. The four things that predict success are:

- Punctuality. Show up on time for the interview and be on time for the first month.
- Honesty about what they do not know. Overconfident technicians cause rework.
- Willingness to be corrected. A technician who argues with a QC inspection is a problem.
- Cleanliness. A technician who leaves their tools scattered will leave parts scattered too.

## The trial task

Do not hire from an interview alone. Give every candidate a paid half-day trial with a real job card. Watch how they:

- Inspect a vehicle
- Log their findings
- Ask for parts
- Handle a customer interaction

A skilled technician who cannot log properly will cost you more than an average technician who follows the process.

## Onboarding

The first two weeks determine whether the hire works. Structure them:

- Week 1: shadow an experienced technician on every job. Do not touch a job card alone.
- Week 2: handle simple jobs solo, with QC on everything.
- Week 3 onwards: full jobs with spot QC on one in five.

## Pay structure

Base salary plus a productivity bonus works better than flat pay. But the bonus must reward the right things:

- Billable hours
- Customer satisfaction scores
- Rework rate below target

A bonus based only on volume encourages rushed work. A bonus on volume plus quality keeps both aligned.

## Retention

Technicians leave for three reasons: pay, boredom, or a bad boss.

Pay you can address. Boredom you address by giving them harder jobs as they grow. Bad boss is on you.

## Training is continuous

Every month, run a 90-minute training session on either a new vehicle system, a new diagnostic tool, or a customer interaction skill. Rotate the lead so different technicians teach.

## How Gariclaim helps

Gariclaim tracks each technician's jobs, billed hours, and rework rate. You can see who is productive, who is idle, and who is generating returns.

The job card history for each technician becomes an informal performance record, which makes promotions and bonuses easier to justify.

[Start a free trial](https://garage.gariclaim.co.ke) and build a team you can rely on.
"""
    },
    # ---- 11 ----
    {
        "date": "2025-03-26", "category": "Operations",
        "slug": "vehicle-inspection-and-qc-in-auto-repair-shops",
        "title": "A Guide to Vehicle Inspection and QC in Auto Repair Shops",
        "description": "How to run consistent quality checks in a Kenyan garage, from intake inspection to final release.",
        "keywords": "vehicle inspection Kenya, garage QC process, auto repair quality control",
        "body": """
A customer will forgive a two-day delay. They will not forgive getting their car back with the same fault they reported.

Quality control is what separates a garage that builds reputation from one that keeps chasing new customers.

## The three QC checkpoints

Every job should pass three quality gates:

1. Intake inspection. Before any work, document the vehicle's condition.
2. Pre-release inspection. Once work is done, verify against the original job card.
3. Release and sign-off. The customer inspects and signs before the vehicle leaves.

## Intake inspection

This protects both you and the customer. Walk around the vehicle with the customer present. Photograph:

- All four corners
- Any existing damage
- The odometer
- The interior if you will enter it
- Any warning lights on the dashboard

Log the customer's description of the fault in their own words. Do not paraphrase.

## Pre-release inspection

This is where most Kenyan garages skip and later regret.

A senior technician, not the person who did the job, checks:

- Every item on the original job card
- All replaced parts are documented
- No tools or rags left in the engine bay or interior
- Fluid levels topped up
- Test drive completed
- Warning lights reset

The QC technician signs the job card. If anything is off, the job goes back.

## The release sign-off

The customer walks around the vehicle with you, checks that the fix works, and signs a release letter. This letter acknowledges:

- The work performed
- The parts replaced
- The cost
- That the vehicle was released in good condition

Signed releases eliminate 90 percent of post-release disputes.

## Common QC failures in Kenyan garages

The most frequent issues we see:

- No separate QC step. The person who did the job signs it off themselves.
- Rushed QC on Friday afternoon. Pressure to release before the weekend.
- No test drive after major repairs.
- Cleaning and detailing skipped, so the customer finds grease on the steering wheel.

## When to hold a vehicle

If QC finds an issue, hold the vehicle. Do not release it with a promise to fix it next week. Once it leaves the yard, the fix becomes a fight.

## How Gariclaim helps

Gariclaim has a dedicated QC and inspection step in every job card. The QC technician is separate from the repair technician, before and after photos are attached, and a customer satisfaction note is captured on release.

Every release is signed and stored against the job card.

[Start a free trial](https://garage.gariclaim.co.ke) and run a QC process you can trust.
"""
    },
    # ---- 12 ----
    {
        "date": "2025-04-02", "category": "Customer Service",
        "slug": "managing-customer-complaints-in-a-kenyan-garage",
        "title": "Managing Customer Complaints in a Kenyan Garage",
        "description": "How to handle unhappy customers so they leave as loyal advocates rather than one-star reviewers.",
        "keywords": "customer complaints garage, customer service auto repair Kenya, handle unhappy customer",
        "body": """
Every garage gets complaints. A repair that did not fix the issue. A bill higher than the quote. A part that failed early.

The garages that thrive are not the ones with no complaints. They are the ones that handle complaints well.

## The 5-step complaint process

1. Listen without interrupting. Let the customer say everything first.
2. Acknowledge the specific issue. Not a generic apology. Name it.
3. Investigate before defending. Look at the job card, photos, and parts log before you respond.
4. Offer a specific fix. A concrete action with a timeline.
5. Follow up. Call two days later to confirm the customer is satisfied.

## What not to do

The three responses that guarantee escalation:

- Arguing with the customer. Even if you are right, they will not hear it in the moment.
- Blaming a technician in front of the customer. It undermines your team and does not solve the problem.
- Promising things you cannot deliver. A rushed timeline to placate the customer creates a second complaint.

## When the garage is wrong

If the repair was defective, own it. Fix it at no cost. Do not argue about whether it was "really" your fault.

The cost of a free rework is small. The cost of a one-star Google review is not.

## When the customer is wrong

Sometimes the customer is wrong. A part failed because they ignored a service interval, or the fault is different from the original one.

In these cases, be factual but respectful. Show the evidence. Offer a fair solution even if you are not at fault. A small discount today buys a customer for years.

## The complaint log

Every complaint should be logged with the customer name, vehicle, job card reference, issue, resolution, and cost to the garage.

Over time, patterns emerge. If the same complaint comes up repeatedly, the problem is systemic, not individual.

## Preventing complaints before they happen

Most complaints trace back to communication gaps, not work quality.

- Confirm the scope in writing
- Take before and after photos
- Tell the customer the price before starting
- Give a realistic timeline

Get those four right and 80 percent of complaints never happen.

## How Gariclaim helps

Gariclaim keeps the full history of every job: job card, authorisation letter, photos, parts used, invoice, and signed release.

When a complaint comes in, you have all the evidence in one place. You can investigate and respond within the hour, often on the same call.

[Start a free trial](https://garage.gariclaim.co.ke) and turn complaints into loyalty.
"""
    },
    # ---- 13 ----
    {
        "date": "2025-04-09", "category": "Operations",
        "slug": "transitioning-from-paper-job-cards-to-digital",
        "title": "Transitioning from Paper Job Cards to Digital",
        "description": "A step-by-step migration plan for moving a Kenyan garage from paper-based processes to a digital system without disrupting operations.",
        "keywords": "digital job cards Kenya, move from paper garage, garage software migration",
        "body": """
Moving from paper to digital is the right decision for any garage past 10 jobs a week. But done badly, it causes chaos. Technicians resent it, records fall into two systems, and after two months you quietly go back to paper.

Here is the migration plan that works.

## Do not do a big bang switch

The single most common failure is trying to go fully digital in one day. You lose two weeks of productivity and morale.

Instead, migrate one function at a time over four to six weeks.

## Week 1: vehicle and customer records

Do not touch job cards yet. Just digitise your customer and vehicle database.

- Enter every active customer
- Enter every vehicle with plate, VIN, make, model
- Link each vehicle to its owner

This is the foundation. Do not skip it.

## Week 2: job card creation only

Start using digital job cards for new jobs. Keep paper alongside for one more week.

Front desk opens the job in the system. Technicians still write on paper as before. At end of week, compare: does the digital card match the paper one?

If yes, proceed. If not, the process has gaps to close.

## Week 3: parts logging

Turn on inventory. Log every part pulled against a job card.

This is the step that causes the most resistance because it slows down technicians in the short term. Expect complaints. Push through.

By Friday, the stock count should match the system count within 5 percent. If it does not, investigate before proceeding.

## Week 4: invoicing and payments

Start invoicing from completed job cards only. Stop raising invoices from the paper stack.

Customers should not notice any difference. Their invoice still looks the same, just now generated from the system.

## Week 5: POS and walk-in sales

Move counter sales onto the digital POS. Print thermal receipts for every sale.

## Week 6: kill the paper

Stop printing blank job cards. Any job that arrives on paper gets entered into the system before work starts. The paper becomes a scratch pad, not a record.

## Training schedule

Do not train everyone at once. Train in three small sessions:

- Session 1: front desk (2 hours)
- Session 2: technicians (1 hour, focused on the app)
- Session 3: accountant or bookkeeper (2 hours)

Follow up after 1 week and 4 weeks for refreshers.

## Handling resistance

The main objections you will hear:

- "This slows me down." It does, for two weeks. Then it is faster.
- "I don't trust the computer." Backups are daily. Nothing gets lost.
- "We've always done it this way." And it has cost you money for years.

Be patient but firm. The migration is not optional.

## How Gariclaim helps

Gariclaim was designed for garages coming from paper. The interface uses the same terms technicians already know: job card, quotation, release, LPO, insurance job.

Onboarding support is available for every new customer.

[Start a free trial](https://garage.gariclaim.co.ke) and take the leap with a system built for the way you already work.
"""
    },
    # ---- 14 ----
    {
        "date": "2025-04-16", "category": "Growth",
        "slug": "multi-branch-garage-management-in-kenya",
        "title": "Multi-Branch Garage Management in Kenya",
        "description": "How to run multiple garage branches under one organisation without losing visibility or control.",
        "keywords": "multi-branch garage Kenya, garage chain management, garage branches",
        "body": """
Running one garage is hard. Running three is a different business entirely.

The problems that scale with more branches:

- Each branch runs its own books, and consolidation is a monthly nightmare
- Inventory moves between branches with no record
- Customers call the wrong branch
- You spend half your week driving between locations

Here is how to structure the operation so it scales.

## One system, many branches

The single most important decision is to run all branches on one system. Not three separate systems with three separate logins and three separate sets of books.

One system gives you:

- A consolidated view of revenue, cost, and profit across all branches
- Inter-branch transfers of stock with a proper audit trail
- Centralised customer records so a customer can service at any branch
- One chart of accounts, one VAT return, one set of financial statements

## Branch manager autonomy with central control

Give each branch manager operational autonomy: staff scheduling, daily customer interactions, small purchasing decisions.

Keep central: pricing, brand standards, large procurement, payroll, tax filings.

Write this down as a policy. Otherwise every branch manager will interpret the boundary differently.

## Inter-branch stock transfers

When Branch A has excess brake pads and Branch B needs them, that transfer must be logged. Without a record, Branch A shows a loss and Branch B shows free stock.

The transfer should reference a transfer document, with both branches confirming receipt.

## Performance comparison

With a single system, you can compare branches on the same metrics:

- Revenue per bay
- Utilisation rate
- Average job value
- Parts margin
- Rework rate

Rank them monthly. Share the numbers with all branch managers. Nothing drives improvement faster than visible comparison.

## Central payroll, local timesheets

Payroll runs centrally because statutory filings are one per entity, not one per branch.

But timesheets, leave requests, and shift schedules run at the branch. Each branch manager approves their own team's time, and payroll uses the approved data.

## Insurance and fleet customers

For insurance and fleet customers, they usually want one invoice, not three. Configure the system so that work done at any branch can be billed on a consolidated monthly invoice.

## What breaks first

The two things that break first when you scale past three branches:

1. Your bank reconciliation. Multiple bank accounts, multiple branches, one accountant.
2. Your month-end close. You spend days consolidating numbers instead of running the business.

Both are solved by running on one system with one chart of accounts.

## How Gariclaim helps

Gariclaim supports multiple branches under one organisation. Stock moves between branches with a transfer record. Reports consolidate automatically. Payroll runs centrally while timesheets and leave are approved per branch.

The Advanced plan supports up to 5 branches and 30 users. If you need more, talk to us.

[Start a free trial](https://garage.gariclaim.co.ke) and scale without chaos.
"""
    },
    # ---- 15 ----
    {
        "date": "2025-04-23", "category": "Finance",
        "slug": "calculating-garage-profitability-simple-framework",
        "title": "Calculating Garage Profitability: A Simple Framework",
        "description": "How to work out whether your Kenyan garage is actually making money, and where the profit leaks are.",
        "keywords": "garage profitability Kenya, auto repair profit margin, garage cash flow",
        "body": """
Most Kenyan garage owners know their monthly revenue. Very few know their monthly profit. The two numbers are completely different, and confusing them is why so many garages feel busy but broke.

Here is the framework.

## Start with gross profit, not revenue

Revenue is what customers pay you. Gross profit is what is left after the direct cost of the work.

For a garage, direct costs are:

- Parts used on jobs
- Technician wages for time spent on jobs
- Subcontractor fees (e.g., specialist machine work)
- Consumables (oil, rags, cleaning supplies)

Gross profit = Revenue − Direct costs

A healthy garage runs 45 to 60 percent gross margin. Below 40 percent suggests pricing is too low, or parts cost is out of control, or technicians are not productive.

## Then operating expenses

From gross profit, subtract operating expenses:

- Rent
- Utilities
- Front desk and management salaries
- Marketing
- Software subscriptions
- Insurance
- Licences
- Vehicle running costs (for courtesy cars or pickup)
- Bank charges and M-Pesa fees

What is left is operating profit, or EBIT.

## Then financing and tax

Subtract:

- Loan interest
- Asset hire purchase charges
- Tax (corporate tax on the profit)

What is left is net profit. That is the number that is actually yours.

## Common profit leaks in Kenyan garages

Five leaks account for most of the missing money:

1. Parts written off as used when they were not. Track this.
2. Wasted labour. Technicians working on the wrong car or idle.
3. Discounts given informally. Every discount reduces margin by the same percentage.
4. Rework. Every warranty repair is pure cost.
5. Bad debt. Customers who never pay, or pay 90 days late.

Fixing any one of these adds 3 to 5 percentage points to net margin.

## Cash flow vs profit

A garage can be profitable and still run out of cash. The two killers:

- Slow-paying insurance customers
- Too much cash tied up in inventory

If your receivables average 60 days and your payables are 30 days, you are financing your customers' business with your own cash.

Track cash flow weekly, not monthly. Even a simple spreadsheet with opening balance, receipts, payments, and closing balance tells you what you need to know.

## A monthly routine

On the 5th of each month:

1. Close the previous month's books
2. Run the P&L
3. Compare to last month and to budget
4. Pick one number to improve this month

Track the improvement. Over a year, small changes compound.

## How Gariclaim helps

Gariclaim generates a P&L, balance sheet, and cash flow statement automatically from your job cards, invoices, and payments. No spreadsheets, no month-end panic.

Because parts, labour, and expenses are all logged in the system, your profit number is real, not estimated.

[Start a free trial](https://garage.gariclaim.co.ke) and finally know your real profit.
"""
    },
    # ---- 16 ----
    {
        "date": "2025-04-30", "category": "Customer Service",
        "slug": "warranty-management-for-garage-repairs-in-kenya",
        "title": "Warranty Management for Garage Repairs in Kenya",
        "description": "How to define, offer, and honour warranties on garage work without eating the cost of every comeback.",
        "keywords": "garage warranty Kenya, auto repair warranty policy, warranty claim garage",
        "body": """
Every garage has a warranty policy. Most are verbal, inconsistent, and impossible to enforce.

A written warranty protects the customer, protects the technician, and protects your cash flow.

## What a warranty should cover

Two distinct things:

1. Workmanship warranty. If the repair fails because of how it was done, you fix it free.
2. Parts warranty. If the part itself fails within its manufacturer's warranty, the supplier covers the replacement.

Keep these separate in the customer's mind.

## Typical warranty periods in Kenya

For workmanship:

- General repairs: 30 days
- Engine work: 90 days
- Electrical and diagnostic: 30 days
- Bodywork and paint: 90 days

For parts, pass through whatever the manufacturer offers. Do not extend it beyond that.

## What a warranty does not cover

State the exclusions clearly. The common ones:

- Wear and tear on consumables (brake pads, oil, filters)
- Damage from continued driving after a fault was reported
- Third-party modifications or repairs
- Accidents or misuse
- Parts supplied by the customer

Put these in writing. Signed at release.

## Handling a warranty claim

When a customer returns with a warranty claim:

1. Look up the original job card. Every job card should be searchable by vehicle or customer.
2. Photograph the current condition.
3. Determine whether the failure is covered.
4. If covered, fix it at no cost. Document the rework against the original job.
5. If not covered, explain the exclusion and offer a fair price.

Do not argue with the customer. Show them the job card, the parts log, and the warranty terms.

## Tracking warranty cost

Every warranty repair has a cost: parts, labour, and lost bay time.

Log it. Track it monthly. If warranty cost exceeds 3 percent of revenue, either your work quality is dropping or your warranty terms are too generous.

## The customer value of a strong warranty

A written warranty is a sales tool, not just a liability.

Advertise it. "90-day workmanship warranty on all engine repairs" is a stronger message than any discount.

## How Gariclaim helps

Gariclaim keeps the complete history of every job: job card, parts used, technician, and signed release. When a warranty claim comes in, you find the original job in seconds.

Warranty rework is logged separately, so you always know what your warranty policy costs you.

[Start a free trial](https://garage.gariclaim.co.ke) and honour your warranty with confidence.
"""
    },
    # ---- 17 ----
    {
        "date": "2025-05-07", "category": "Inventory",
        "slug": "guide-to-pricing-spare-parts-for-kenyan-garages",
        "title": "A Guide to Pricing Spare Parts for Kenyan Garages",
        "description": "How to set and maintain part pricing so you stay competitive without eroding margin.",
        "keywords": "spare parts pricing Kenya, auto parts markup, garage parts margin",
        "body": """
Parts pricing in Kenyan garages is often set by habit. The same markup has been applied for years, without revisiting whether it still makes sense.

Here is a pricing framework you can actually defend.

## Start with landed cost

The price you pay your supplier is not the cost of the part. The landed cost includes:

- Purchase price
- Transport to your garage
- Import duty and VAT (if applicable)
- Any packaging or handling

If you ignore these, you are marking up a number that is already below your real cost.

## Segment parts by type

Different parts warrant different margins. A rough starting point:

- Fast-moving consumables (oil, filters, wipers): 25 to 35 percent markup
- Common replacement parts (brake pads, batteries): 25 to 35 percent
- Specialist or OEM parts: 35 to 50 percent
- Rare or imported parts: 40 to 60 percent

Higher markup on rare parts is justified because of the risk of holding dead stock.

## Do not hide markup in labour

Some garages keep parts markup low and load profit into the labour rate. Customers eventually notice, and it damages trust.

Keep both lines honest. Mark up parts fairly. Charge labour fairly. Show both on the invoice.

## Price lists by customer type

Different customers warrant different price lists:

- Retail walk-in: full margin
- Regular trade customers: 5 to 10 percent discount
- Fleet accounts: negotiated, volume-based
- Insurance: per the assessment agreed with the insurer

Gariclaim supports multiple price lists per customer, so each sale uses the right one automatically.

## Reviewing prices regularly

Review parts pricing every quarter. Supplier costs move. The shilling moves. Your prices should adjust accordingly.

If you have not raised parts prices in two years, your margin has quietly disappeared.

## The dead stock problem

Every garage accumulates dead stock: parts bought for a job that never happened, or for a model that no longer comes in.

Rule: if a part has not moved in 12 months, discount it. 20 to 30 percent off is better than carrying it forever.

Every three months, run a dead stock report and act on it.

## When to say no

If a customer asks you to match a price you cannot match, walk away. Losing money on a sale to keep a customer is a slow way to close the business.

## How Gariclaim helps

Gariclaim supports multiple price lists, tracks parts margin by category, and flags slow-moving stock so you can discount before it becomes dead weight.

Every sale, whether from a job card or POS, uses the correct price list for that customer automatically.

[Start a free trial](https://garage.gariclaim.co.ke) and price parts with confidence.
"""
    },
    # ---- 18 ----
    {
        "date": "2025-05-14", "category": "Growth",
        "slug": "how-to-handle-fleet-maintenance-contracts-in-kenya",
        "title": "How to Handle Fleet Maintenance Contracts in Kenya",
        "description": "How to win and manage fleet maintenance contracts with corporate clients, matatu SACCOs, and logistics companies.",
        "keywords": "fleet maintenance Kenya, corporate fleet contract, fleet repair garage",
        "body": """
Fleet contracts are the most stable revenue a Kenyan garage can have. One signed contract can keep three bays busy for a year.

They are also the most demanding customers. Here is how to handle them.

## Who buys fleet maintenance

The main fleet buyers in Kenya:

- Corporate vehicle fleets (banks, telcos, logistics)
- Matatu SACCOs
- Boda boda and courier companies
- NGOs and government agencies
- Car hire and taxi companies

Each has different priorities. Corporates care about uptime and compliance. SACCOs care about cost. NGOs care about audit trail.

## What the contract usually covers

A typical fleet contract includes:

- Scheduled servicing per manufacturer intervals
- Breakdown response and roadside assistance
- Pre-trip inspections
- Minor repairs at an agreed rate card
- Major repairs quoted per job
- Consolidated monthly invoicing
- Fleet-level reporting

Not every contract includes everything. Read the terms carefully before signing.

## Pricing for fleets

Do not offer fleet pricing based on the same rates as retail. Volume discounts are expected, but only where you can afford them.

The discount should come from reduced cost, not reduced margin:

- Fleets mean less marketing, lower cost to acquire
- Predictable volume means better parts purchasing
- Consolidated invoicing means fewer transactions

If those savings do not exist for you, do not sign a deep-discount contract.

## Rate card

Fleet customers want a rate card, not a quote per job. Publish your rates for:

- Per-hour labour, per category of work
- Standard service packages
- Common repair jobs
- Parts markup

The rate card locks in expectations. It also stops the customer negotiating every invoice.

## Payment terms

Most fleet contracts specify 30-day payment. Some push for 60 or 90. Push back on anything beyond 45 unless the customer is very large and very reliable.

Cash flow kills garages faster than low margin. Do not finance a corporate customer's working capital for free.

## Reporting

Fleet customers want monthly reporting. Give them:

- Vehicles serviced
- Repairs done
- Total spend
- Downtime
- Recommendations

The reporting alone justifies the contract for many corporates. It is also a reason they stay with you rather than shop around.

## Consolidate the invoicing

One invoice per month per fleet customer, not one per job. This simplifies their payment process and reduces the chance of a rejected invoice.

Gariclaim supports consolidated monthly billing for fleet customers. Jobs done at any branch roll up into one invoice.

## Renewal

Start the renewal conversation 90 days before the contract expires. Do not wait for the customer to raise it.

Bring the reporting from the year. Show them the value. Ask what would make the next year better.

## How Gariclaim helps

Gariclaim handles fleet jobs the same way as any other job, but rolls them up per customer for consolidated invoicing. Rate cards are set at the customer level. Reporting by fleet customer is built in.

[Start a free trial](https://garage.gariclaim.co.ke) and win your next fleet contract.
"""
    },
    # ---- 19 ----
    {
        "date": "2025-05-21", "category": "Finance",
        "slug": "fixed-asset-management-for-garages",
        "title": "Fixed Asset Management for Garages: Tools, Lifts, and Diagnostic Equipment",
        "description": "How to track, depreciate, and maintain the fixed assets that keep your Kenyan garage running.",
        "keywords": "fixed assets garage Kenya, garage equipment depreciation, asset register garage",
        "body": """
A Kenyan garage typically holds several million shillings in fixed assets: hoists, compressors, diagnostic tools, welders, spray booths, office equipment.

Yet most garages have no asset register. They do not know what they own, what it is worth, or when it needs replacing.

## What counts as a fixed asset

A fixed asset is something you use to run the business, lasting more than one year, that is not sold to customers.

For a garage:

- Vehicle lifts and jacks
- Diagnostic scanners
- Compressors and air tools
- Welders and cutting equipment
- Spray booths and paint mixing stations
- Tyre machines and balancing equipment
- Tool cabinets and hand tools (higher-value sets)
- Office equipment, computers, and software
- Delivery or pickup vehicles

Consumables like oil, filters, and rags are not fixed assets. They are expenses.

## Why you need an asset register

An asset register does five things:

1. Tracks what you own
2. Records the purchase date and cost
3. Calculates depreciation for tax purposes
4. Schedules maintenance
5. Helps you plan replacements and budget for them

Without one, you are guessing.

## Depreciation

KRA allows tax deductions on asset depreciation at specific rates. Common categories for garages:

- Computer hardware and software: 33.3 percent per year (3-year life)
- Vehicles: 25 percent per year
- Plant and machinery (lifts, welders, diagnostic equipment): 12.5 percent per year
- Furniture and fittings: 12.5 percent per year

You claim this depreciation on your annual income tax return. Without an asset register, you cannot claim it accurately.

## Tracking maintenance

Every asset needs scheduled maintenance. Lifts need annual inspections. Compressors need oil changes. Diagnostic tools need software updates.

Log these in the asset register with next-due dates.

## Planning replacements

An asset approaching the end of its useful life should have a replacement plan. Lifts typically last 15 to 20 years. Diagnostic tools last 5 to 8. Compressors last 10 to 15.

Budget a replacement fund monthly. Set aside a small percentage of revenue for asset renewal.

## When to repair vs replace

The rule of thumb: if annual repair cost exceeds 40 percent of the new replacement cost, replace it.

For example, if a compressor costs KES 200,000 new and is costing you KES 85,000 a year to keep running, replace it.

## Insurance

Every fixed asset should be insured. A fire, theft, or flood can wipe out years of investment in one night.

Review coverage annually. Values go up over time. Under-insured assets are a common mistake.

## How Gariclaim helps

Gariclaim includes a fixed asset register that tracks purchase dates, cost, depreciation, and maintenance schedule. Depreciation is calculated automatically and flows into your financial statements.

The adjusting entries for depreciation are generated at year end without manual journal entries.

[Start a free trial](https://garage.gariclaim.co.ke) and finally know what you own.
"""
    },
    # ---- 20 ----
    {
        "date": "2025-05-28", "category": "Tax & Compliance",
        "slug": "year-end-accounting-checklist-for-kenyan-garages",
        "title": "Year-End Accounting Checklist for Kenyan Garages",
        "description": "Everything a Kenyan garage needs to close the books, prepare for tax filing, and start the new year clean.",
        "keywords": "year end accounting garage, KRA annual return, garage tax filing Kenya",
        "body": """
Every garage owner dreads year end. It is the moment you discover that six months of transactions were never recorded, receipts are in a shoebox, and the accountant wants everything by Friday.

Here is how to close the year without panic.

## Two weeks before year end

Start early. The last two weeks of the year are for confirming, not starting.

- Reconcile every bank account to the last statement
- Reconcile M-Pesa to the last statement
- Confirm supplier balances with a statement request
- Confirm customer balances with a statement send
- Count physical stock and compare to system

## The week of year end

The final week is for closing out.

- Ensure all December invoices are issued
- Ensure all December expenses are recorded
- Accrue any expenses you incurred but have not yet received invoices for
- Accrue income you earned but have not yet invoiced

Accruals matter. Without them, the year's profit is understated or overstated depending on which side is missing.

## Closing entries

Your accountant or bookkeeper will make closing entries:

- Depreciate fixed assets for the year
- Adjust inventory to physical count
- Write off bad debts you will not collect
- Recognise deferred income that has now been earned
- Post any final adjustments

Do not skip these. They are what turn raw transactions into financial statements.

## Financial statements to produce

At year end, produce:

- Profit and loss statement for the year
- Balance sheet as at year end
- Cash flow statement
- Supporting schedules for receivables, payables, and fixed assets

These are the documents your auditor needs, KRA needs, and your bank needs if you are applying for credit.

## KRA filings

Depending on your structure and obligations:

- Annual income tax return (individuals by 30 June; companies within 6 months of financial year end)
- VAT returns for December (due 20 January)
- PAYE for December (due 9 January)

Do not miss these dates. Penalties compound fast.

## Records retention

Keep for a minimum of 5 years:

- Invoices issued and received
- Bank and M-Pesa statements
- Payroll records
- VAT returns filed
- Asset purchase records

Keep them digitally where possible. Paper degrades. Digital does not.

## Setting up for a clean new year

Before you close the year, set up next year's books:

- Carry forward opening balances
- Set up the new year's accounting period
- Update employee salary rates if applicable
- Reset leave balances
- Update price lists

Done properly, this takes an hour. Done badly, it takes three months of cleanup.

## How Gariclaim helps

Gariclaim generates year-end financial statements automatically from your recorded transactions. Depreciation, accruals, and adjustments are supported as journal entries. Reports export to PDF or Excel for your accountant.

Your KRA PIN, tax registration types, and filing history are all stored against your organisation profile.

[Start a free trial](https://garage.gariclaim.co.ke) and end this year without the panic.
"""
    },
]

# Write each post
output_dir = Path("_posts")
output_dir.mkdir(exist_ok=True)
count = 0

for post in POSTS:
    filename = f"{post['date']}-{post['slug']}.md"
    filepath = output_dir / filename

    content = f"""---
layout: post
title: "{post['title']}"
description: "{post['description']}"
category: {post['category']}
author: Gariclaim
keywords: "{post['keywords']}"
---

{post['body'].strip()}
"""
    filepath.write_text(content)
    count += 1
    print(f"OK  {filename}")

print()
print(f"Generated {count} posts in _posts/")
