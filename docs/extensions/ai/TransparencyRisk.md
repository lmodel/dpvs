---
search:
  boost: 10.0
---

# Class: TransparencyRisk 


_Risk that an AI's design, performance, outputs, or other characteristics_

_are not sufficiently transparent_



<div data-search-exclude markdown="1">



URI: [ai:TransparencyRisk](https://w3id.org/lmodel/dpv/ai/TransparencyRisk)





```mermaid
 classDiagram
    class TransparencyRisk
    click TransparencyRisk href "../TransparencyRisk/"
      RiskConcept <|-- TransparencyRisk
        click RiskConcept href "../RiskConcept/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **TransparencyRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TransparencyRisk](https://w3id.org/lmodel/dpv/ai/TransparencyRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Transparency Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TransparencyRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TransparencyRisk |
| native | ai:TransparencyRisk |
| exact | dpv_ai:TransparencyRisk, dpv_ai_owl:TransparencyRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TransparencyRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TransparencyRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk that an AI''s design, performance, outputs, or other characteristics

  are not sufficiently transparent'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Transparency Risk
exact_mappings:
- dpv_ai:TransparencyRisk
- dpv_ai_owl:TransparencyRisk
is_a: RiskConcept
class_uri: ai:TransparencyRisk

```
</details>

### Induced

<details>
```yaml
name: TransparencyRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TransparencyRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk that an AI''s design, performance, outputs, or other characteristics

  are not sufficiently transparent'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Transparency Risk
exact_mappings:
- dpv_ai:TransparencyRisk
- dpv_ai_owl:TransparencyRisk
is_a: RiskConcept
class_uri: ai:TransparencyRisk

```
</details></div>