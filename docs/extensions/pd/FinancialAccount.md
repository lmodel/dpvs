---
search:
  boost: 10.0
---

# Class: FinancialAccount 


_Information about financial accounts_



<div data-search-exclude markdown="1">



URI: [pd:FinancialAccount](https://w3id.org/lmodel/dpv/pd/FinancialAccount)





```mermaid
 classDiagram
    class FinancialAccount
    click FinancialAccount href "../FinancialAccount/"
      Financial <|-- FinancialAccount
        click Financial href "../Financial/"
      

      FinancialAccount <|-- AccountIdentifier
        click AccountIdentifier href "../AccountIdentifier/"
      FinancialAccount <|-- BankAccount
        click BankAccount href "../BankAccount/"
      FinancialAccount <|-- PaymentCard
        click PaymentCard href "../PaymentCard/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * **FinancialAccount**
        * [AccountIdentifier](AccountIdentifier.md)
        * [BankAccount](BankAccount.md)
        * [PaymentCard](PaymentCard.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FinancialAccount](https://w3id.org/lmodel/dpv/pd/FinancialAccount) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Financial Account




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FinancialAccount |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FinancialAccount |
| native | pd:FinancialAccount |
| exact | dpv_pd:FinancialAccount, dpv_pd_owl:FinancialAccount |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FinancialAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial accounts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Account
exact_mappings:
- dpv_pd:FinancialAccount
- dpv_pd_owl:FinancialAccount
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Financial
class_uri: pd:FinancialAccount

```
</details>

### Induced

<details>
```yaml
name: FinancialAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial accounts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Account
exact_mappings:
- dpv_pd:FinancialAccount
- dpv_pd_owl:FinancialAccount
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Financial
class_uri: pd:FinancialAccount

```
</details></div>