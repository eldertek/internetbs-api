class GenericResult:
    def __init__(self, transactid, status, message):
        self.transactid = transactid
        self.status = status
        self.message = message

    def __str__(self):
        return f"GenericResult(status={self.status}, message={self.message})"

# Domain
class DomainCheckResult:
    def __init__(self, transactid, status, domain, minregperiod, maxregperiod, registrarlockallowed, privatewhoisallowed, realtimeregistration):
        self.transactid = transactid
        self.status = status
        self.domain = domain
        self.minregperiod = minregperiod
        self.maxregperiod = maxregperiod
        self.registrarlockallowed = registrarlockallowed
        self.privatewhoisallowed = privatewhoisallowed
        self.realtimeregistration = realtimeregistration

    def __str__(self):
        return f"DomainCheckResult(status={self.status}, domain={self.domain})"

class DomainCreateResult:
    def __init__(self, transactid, status, currency, price, product):
        self.transactid = transactid
        self.status = status
        self.currency = currency
        self.price = price
        self.product = product

    def __str__(self):
        return f"DomainCreateResult(status={self.status}, currency={self.currency}, price={self.price}, product={self.product})"

class DomainUpdateResult:
    def __init__(self, transactid, status, message):
        self.transactid = transactid
        self.status = status
        self.message = message

    def __str__(self):
        return f"DomainUpdateResult(status={self.status}, message={self.message})"

class DomainInfoResult:
    def __init__(self, transactid, status, domain, expirationdate, registrationdate, paiduntil, registrarlock, autorenew, privatewhois, whoisprivacy, domainstatus, contacts, transferauthinfo, dnssec, price):
        self.transactid = transactid
        self.status = status
        self.domain = domain
        self.expirationdate = expirationdate
        self.registrationdate = registrationdate
        self.paiduntil = paiduntil
        self.registrarlock = registrarlock
        self.autorenew = autorenew
        self.privatewhois = privatewhois
        self.whoisprivacy = whoisprivacy
        self.domainstatus = domainstatus
        self.contacts = contacts
        self.transferauthinfo = transferauthinfo
        self.dnssec = dnssec
        self.price = price

    def __str__(self):
        return f"DomainInfoResult(status={self.status}, domain={self.domain})"

class DomainRegistryStatusResult:
    def __init__(self, transactid, domain, registrystatus, status):
        self.transactid = transactid
        self.domain = domain
        self.registrystatus = registrystatus
        self.status = status

    def __str__(self):
        return f"DomainRegistryStatusResult(status={self.status}, domain={self.domain}, registrystatus={self.registrystatus})"

class DomainItem:
    def __init__(self, domain_name):
        self.domain_name = domain_name

    def __str__(self):
        return f"DomainItem(domain_name={self.domain_name})"
    
# DNS
class DNSAddRecordResult:
    def __init__(self, transactid, status):
        self.transactid = transactid
        self.status = status

    def __str__(self):
        return f"DNSAddRecordResult(status={self.status}, transactid={self.transactid})"

class DNSRemoveRecordResult:
    def __init__(self, transactid, status):
        self.transactid = transactid
        self.status = status

    def __str__(self):
        return f"DNSRemoveRecordResult(status={self.status}, transactid={self.transactid})"

class DNSUpdateRecordResult:
    def __init__(self, transactid, status):
        self.transactid = transactid
        self.status = status
        
    def __str__(self):
        return f"DNSUpdateRecordResult(status={self.status}, transactid={self.transactid})"

class DNSListRecordsResult:
    def __init__(self, transactid, status, records):
        self.transactid = transactid
        self.status = status
        self.records = records

    def __str__(self):
        return f"DNSListRecordsResult(status={self.status}, transactid={self.transactid}, records={self.records})"