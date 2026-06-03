---
search:
  boost: 10.0
---

# Class: Payment 


_Something that acts as or provides payment e.g. to access a service or_

_purchase resources_



<div data-search-exclude markdown="1">



URI: [risk:Payment](https://w3id.org/lmodel/dpv/risk/Payment)





```mermaid
 classDiagram
    class Payment
    click Payment href "../Payment/"
      PotentialConsequence <|-- Payment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Payment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Payment
        click PotentialRisk href "../PotentialRisk/"
      Remuneration <|-- Payment
        click Remuneration href "../Remuneration/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Remuneration](Remuneration.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Payment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Payment](https://w3id.org/lmodel/dpv/risk/Payment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Payment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Payment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Payment |
| native | risk:Payment |
| exact | dpv_risk:Payment, dpv_risk_owl:Payment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Payment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Payment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides payment e.g. to access a service
  or

  purchase resources'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Payment
exact_mappings:
- dpv_risk:Payment
- dpv_risk_owl:Payment
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Payment

```
</details>

### Induced

<details>
```yaml
name: Payment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Payment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides payment e.g. to access a service
  or

  purchase resources'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Payment
exact_mappings:
- dpv_risk:Payment
- dpv_risk_owl:Payment
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Payment

```
</details></div>