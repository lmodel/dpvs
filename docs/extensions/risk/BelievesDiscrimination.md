---
search:
  boost: 10.0
---

# Class: BelievesDiscrimination 


_Discrimination based on a person's beliefs or practices_



<div data-search-exclude markdown="1">



URI: [risk:BelievesDiscrimination](https://w3id.org/lmodel/dpv/risk/BelievesDiscrimination)





```mermaid
 classDiagram
    class BelievesDiscrimination
    click BelievesDiscrimination href "../BelievesDiscrimination/"
      PotentialConsequence <|-- BelievesDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- BelievesDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- BelievesDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- BelievesDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **BelievesDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:BelievesDiscrimination](https://w3id.org/lmodel/dpv/risk/BelievesDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Believes Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#BelievesDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:BelievesDiscrimination |
| native | risk:BelievesDiscrimination |
| exact | dpv_risk:BelievesDiscrimination, dpv_risk_owl:BelievesDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BelievesDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BelievesDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's beliefs or practices
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Believes Discrimination
exact_mappings:
- dpv_risk:BelievesDiscrimination
- dpv_risk_owl:BelievesDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:BelievesDiscrimination

```
</details>

### Induced

<details>
```yaml
name: BelievesDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BelievesDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's beliefs or practices
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Believes Discrimination
exact_mappings:
- dpv_risk:BelievesDiscrimination
- dpv_risk_owl:BelievesDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:BelievesDiscrimination

```
</details></div>