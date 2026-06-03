---
search:
  boost: 10.0
---

# Class: Reward 


_Something that acts as or provides rewards i.e. a benefit given for some_

_service or activity that is not a payment or fee_



<div data-search-exclude markdown="1">



URI: [risk:Reward](https://w3id.org/lmodel/dpv/risk/Reward)





```mermaid
 classDiagram
    class Reward
    click Reward href "../Reward/"
      PotentialConsequence <|-- Reward
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Reward
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Reward
        click PotentialRisk href "../PotentialRisk/"
      Remuneration <|-- Reward
        click Remuneration href "../Remuneration/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Remuneration](Remuneration.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Reward** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Reward](https://w3id.org/lmodel/dpv/risk/Reward) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reward




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Reward |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Reward |
| native | risk:Reward |
| exact | dpv_risk:Reward, dpv_risk_owl:Reward |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Reward
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Reward
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides rewards i.e. a benefit given for
  some

  service or activity that is not a payment or fee'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reward
exact_mappings:
- dpv_risk:Reward
- dpv_risk_owl:Reward
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Reward

```
</details>

### Induced

<details>
```yaml
name: Reward
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Reward
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides rewards i.e. a benefit given for
  some

  service or activity that is not a payment or fee'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reward
exact_mappings:
- dpv_risk:Reward
- dpv_risk_owl:Reward
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Reward

```
</details></div>