---
search:
  boost: 10.0
---

# Class: InformationRequired 


_Justification that the process is delayed due to additional information_

_being required_



<div data-search-exclude markdown="1">



URI: [justifications:InformationRequired](https://w3id.org/lmodel/dpv/justifications/InformationRequired)





```mermaid
 classDiagram
    class InformationRequired
    click InformationRequired href "../InformationRequired/"
      DelayJustification <|-- InformationRequired
        click DelayJustification href "../DelayJustification/"
      
      
```





## Inheritance
* [DelayJustification](DelayJustification.md)
    * **InformationRequired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:InformationRequired](https://w3id.org/lmodel/dpv/justifications/InformationRequired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Information Required




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#InformationRequired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:InformationRequired |
| native | justifications:InformationRequired |
| exact | dpv_justifications:InformationRequired, dpv_justifications_owl:InformationRequired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InformationRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#InformationRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is delayed due to additional information

  being required'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Information Required
exact_mappings:
- dpv_justifications:InformationRequired
- dpv_justifications_owl:InformationRequired
is_a: DelayJustification
class_uri: justifications:InformationRequired

```
</details>

### Induced

<details>
```yaml
name: InformationRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#InformationRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is delayed due to additional information

  being required'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Information Required
exact_mappings:
- dpv_justifications:InformationRequired
- dpv_justifications_owl:InformationRequired
is_a: DelayJustification
class_uri: justifications:InformationRequired

```
</details></div>