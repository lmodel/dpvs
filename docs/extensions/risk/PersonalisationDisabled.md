---
search:
  boost: 10.0
---

# Class: PersonalisationDisabled 


_Concept representing personalisation disabled_



<div data-search-exclude markdown="1">



URI: [risk:PersonalisationDisabled](https://w3id.org/lmodel/dpv/risk/PersonalisationDisabled)





```mermaid
 classDiagram
    class PersonalisationDisabled
    click PersonalisationDisabled href "../PersonalisationDisabled/"
      PotentialConsequence <|-- PersonalisationDisabled
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PersonalisationDisabled
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PersonalisationDisabled
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- PersonalisationDisabled
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **PersonalisationDisabled** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PersonalisationDisabled](https://w3id.org/lmodel/dpv/risk/PersonalisationDisabled) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Personalisation Disabled




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PersonalisationDisabled |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PersonalisationDisabled |
| native | risk:PersonalisationDisabled |
| exact | dpv_risk:PersonalisationDisabled, dpv_risk_owl:PersonalisationDisabled |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalisationDisabled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalisationDisabled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing personalisation disabled
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personalisation Disabled
exact_mappings:
- dpv_risk:PersonalisationDisabled
- dpv_risk_owl:PersonalisationDisabled
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalisationDisabled

```
</details>

### Induced

<details>
```yaml
name: PersonalisationDisabled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalisationDisabled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing personalisation disabled
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personalisation Disabled
exact_mappings:
- dpv_risk:PersonalisationDisabled
- dpv_risk_owl:PersonalisationDisabled
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalisationDisabled

```
</details></div>