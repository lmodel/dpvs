---
search:
  boost: 10.0
---

# Class: BankAccount 


_Information about bank accounts_



<div data-search-exclude markdown="1">



URI: [pd:BankAccount](https://w3id.org/lmodel/dpv/pd/BankAccount)





```mermaid
 classDiagram
    class BankAccount
    click BankAccount href "../BankAccount/"
      FinancialAccount <|-- BankAccount
        click FinancialAccount href "../FinancialAccount/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * **BankAccount**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BankAccount](https://w3id.org/lmodel/dpv/pd/BankAccount) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Bank Account




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BankAccount |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BankAccount |
| native | pd:BankAccount |
| exact | dpv_pd:BankAccount, dpv_pd_owl:BankAccount |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BankAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BankAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about bank accounts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Bank Account
exact_mappings:
- dpv_pd:BankAccount
- dpv_pd_owl:BankAccount
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: FinancialAccount
class_uri: pd:BankAccount

```
</details>

### Induced

<details>
```yaml
name: BankAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BankAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about bank accounts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Bank Account
exact_mappings:
- dpv_pd:BankAccount
- dpv_pd_owl:BankAccount
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: FinancialAccount
class_uri: pd:BankAccount

```
</details></div>