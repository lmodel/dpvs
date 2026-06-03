---
search:
  boost: 10.0
---

# Class: PersonalisationEnabled 


_Concept representing personalisation enabled_



<div data-search-exclude markdown="1">



URI: [risk:PersonalisationEnabled](https://w3id.org/lmodel/dpv/risk/PersonalisationEnabled)





```mermaid
 classDiagram
    class PersonalisationEnabled
    click PersonalisationEnabled href "../PersonalisationEnabled/"
      PotentialConsequence <|-- PersonalisationEnabled
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PersonalisationEnabled
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PersonalisationEnabled
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- PersonalisationEnabled
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **PersonalisationEnabled** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PersonalisationEnabled](https://w3id.org/lmodel/dpv/risk/PersonalisationEnabled) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Personalisation Enabled




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PersonalisationEnabled |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PersonalisationEnabled |
| native | risk:PersonalisationEnabled |
| exact | dpv_risk:PersonalisationEnabled, dpv_risk_owl:PersonalisationEnabled |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalisationEnabled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalisationEnabled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing personalisation enabled
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personalisation Enabled
exact_mappings:
- dpv_risk:PersonalisationEnabled
- dpv_risk_owl:PersonalisationEnabled
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalisationEnabled

```
</details>

### Induced

<details>
```yaml
name: PersonalisationEnabled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PersonalisationEnabled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing personalisation enabled
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Personalisation Enabled
exact_mappings:
- dpv_risk:PersonalisationEnabled
- dpv_risk_owl:PersonalisationEnabled
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PersonalisationEnabled

```
</details></div>