---
search:
  boost: 10.0
---

# Class: GroupHealthSafety 


_Concept representing health & safety of a group or group(s)_



<div data-search-exclude markdown="1">



URI: [risk:GroupHealthSafety](https://w3id.org/lmodel/dpv/risk/GroupHealthSafety)





```mermaid
 classDiagram
    class GroupHealthSafety
    click GroupHealthSafety href "../GroupHealthSafety/"
      PotentialConsequence <|-- GroupHealthSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- GroupHealthSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- GroupHealthSafety
        click PotentialRisk href "../PotentialRisk/"
      HealthSafety <|-- GroupHealthSafety
        click HealthSafety href "../HealthSafety/"
      GroupRisk <|-- GroupHealthSafety
        click GroupRisk href "../GroupRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [GroupRisk](GroupRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **GroupHealthSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [HealthSafety](HealthSafety.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GroupHealthSafety](https://w3id.org/lmodel/dpv/risk/GroupHealthSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Group Health & Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#GroupHealthSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GroupHealthSafety |
| native | risk:GroupHealthSafety |
| exact | dpv_risk:GroupHealthSafety, dpv_risk_owl:GroupHealthSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health & safety of a group or group(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Group Health & Safety
exact_mappings:
- dpv_risk:GroupHealthSafety
- dpv_risk_owl:GroupHealthSafety
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- HealthSafety
class_uri: risk:GroupHealthSafety

```
</details>

### Induced

<details>
```yaml
name: GroupHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health & safety of a group or group(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Group Health & Safety
exact_mappings:
- dpv_risk:GroupHealthSafety
- dpv_risk_owl:GroupHealthSafety
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- HealthSafety
class_uri: risk:GroupHealthSafety

```
</details></div>