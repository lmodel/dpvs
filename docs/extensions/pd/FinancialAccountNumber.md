---
search:
  boost: 10.0
---

# Class: FinancialAccountNumber 


_Information about financial account number_



<div data-search-exclude markdown="1">



URI: [pd:FinancialAccountNumber](https://w3id.org/lmodel/dpv/pd/FinancialAccountNumber)





```mermaid
 classDiagram
    class FinancialAccountNumber
    click FinancialAccountNumber href "../FinancialAccountNumber/"
      AccountIdentifier <|-- FinancialAccountNumber
        click AccountIdentifier href "../AccountIdentifier/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * [AccountIdentifier](AccountIdentifier.md)
            * **FinancialAccountNumber**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FinancialAccountNumber](https://w3id.org/lmodel/dpv/pd/FinancialAccountNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Financial Account Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FinancialAccountNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FinancialAccountNumber |
| native | pd:FinancialAccountNumber |
| exact | dpv_pd:FinancialAccountNumber, dpv_pd_owl:FinancialAccountNumber |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FinancialAccountNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialAccountNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial account number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Account Number
exact_mappings:
- dpv_pd:FinancialAccountNumber
- dpv_pd_owl:FinancialAccountNumber
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: AccountIdentifier
class_uri: pd:FinancialAccountNumber

```
</details>

### Induced

<details>
```yaml
name: FinancialAccountNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialAccountNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial account number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Account Number
exact_mappings:
- dpv_pd:FinancialAccountNumber
- dpv_pd_owl:FinancialAccountNumber
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: AccountIdentifier
class_uri: pd:FinancialAccountNumber

```
</details></div>