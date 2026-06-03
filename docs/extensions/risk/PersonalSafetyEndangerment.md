---
search:
  boost: 10.0
---

# Class: PersonalSafetyEndangerment 


_Concept representing Personal Safety Endangerment_



<div data-search-exclude markdown="1">



URI: [risk:PersonalSafetyEndangerment](https://w3id.org/lmodel/dpv/risk/PersonalSafetyEndangerment)





```mermaid
 classDiagram
    class PersonalSafetyEndangerment
    click PersonalSafetyEndangerment href "../PersonalSafetyEndangerment/"
      PotentialConsequence <|-- PersonalSafetyEndangerment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PersonalSafetyEndangerment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PersonalSafetyEndangerment
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- PersonalSafetyEndangerment
        click IndividualRisk href "../IndividualRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **PersonalSafetyEndangerment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PersonalSafetyEndangerment](https://w3id.org/lmodel/dpv/risk/PersonalSafetyEndangerment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Personal Safety Endangerment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PersonalSafetyEndangerment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PersonalSafetyEndangerment |
| native | risk:PersonalSafetyEndangerment |
| exact | dpv_risk:PersonalSafetyEndangerment, dpv_risk_owl:PersonalSafetyEndangerment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalSafetyEndangerment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalSafetyEndangerment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Personal Safety Endangerment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personal Safety Endangerment
exact_mappings:
- dpv_risk:PersonalSafetyEndangerment
- dpv_risk_owl:PersonalSafetyEndangerment
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalSafetyEndangerment

```
</details>

### Induced

<details>
```yaml
name: PersonalSafetyEndangerment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalSafetyEndangerment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Personal Safety Endangerment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personal Safety Endangerment
exact_mappings:
- dpv_risk:PersonalSafetyEndangerment
- dpv_risk_owl:PersonalSafetyEndangerment
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalSafetyEndangerment

```
</details></div>