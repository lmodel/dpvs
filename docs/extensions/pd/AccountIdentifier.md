---
search:
  boost: 10.0
---

# Class: AccountIdentifier 


_Information about financial account identifier_



<div data-search-exclude markdown="1">



URI: [pd:AccountIdentifier](https://w3id.org/lmodel/dpv/pd/AccountIdentifier)





```mermaid
 classDiagram
    class AccountIdentifier
    click AccountIdentifier href "../AccountIdentifier/"
      FinancialAccount <|-- AccountIdentifier
        click FinancialAccount href "../FinancialAccount/"
      

      AccountIdentifier <|-- FinancialAccountNumber
        click FinancialAccountNumber href "../FinancialAccountNumber/"
      AccountIdentifier <|-- PaymentCardNumber
        click PaymentCardNumber href "../PaymentCardNumber/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * **AccountIdentifier**
            * [FinancialAccountNumber](FinancialAccountNumber.md)
            * [PaymentCardNumber](PaymentCardNumber.md) [ [PaymentCard](PaymentCard.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:AccountIdentifier](https://w3id.org/lmodel/dpv/pd/AccountIdentifier) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Account Identifier




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#AccountIdentifier |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:AccountIdentifier |
| native | pd:AccountIdentifier |
| exact | dpv_pd:AccountIdentifier, dpv_pd_owl:AccountIdentifier |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccountIdentifier
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AccountIdentifier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial account identifier
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Account Identifier
exact_mappings:
- dpv_pd:AccountIdentifier
- dpv_pd_owl:AccountIdentifier
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: FinancialAccount
class_uri: pd:AccountIdentifier

```
</details>

### Induced

<details>
```yaml
name: AccountIdentifier
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AccountIdentifier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial account identifier
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Account Identifier
exact_mappings:
- dpv_pd:AccountIdentifier
- dpv_pd_owl:AccountIdentifier
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: FinancialAccount
class_uri: pd:AccountIdentifier

```
</details></div>