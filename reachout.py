from company import Company
from email_builder import FirstLastEmailBuilder

companies = {
    "Roblox": Company('Roblox', FirstLastEmailBuilder("@roblox.com"))
}


def create_drafts(company: Company):
    company.create_drafts()


# create_drafts(companies["Roblox"])
