---
search:
  boost: 10.0
---

# Class: ObjectivesImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it impairs the objectives of associated context_



<div data-search-exclude markdown="1">



URI: [justifications:ObjectivesImpaired](https://w3id.org/lmodel/dpv/justifications/ObjectivesImpaired)





```mermaid
 classDiagram
    class ObjectivesImpaired
    click ObjectivesImpaired href "../ObjectivesImpaired/"
      NonFulfilmentJustification <|-- ObjectivesImpaired
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **ObjectivesImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ObjectivesImpaired](https://w3id.org/lmodel/dpv/justifications/ObjectivesImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Objectives Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ObjectivesImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ObjectivesImpaired |
| native | justifications:ObjectivesImpaired |
| exact | dpv_justifications:ObjectivesImpaired, dpv_justifications_owl:ObjectivesImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ObjectivesImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ObjectivesImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it impairs the objectives of associated context'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Objectives Impaired
exact_mappings:
- dpv_justifications:ObjectivesImpaired
- dpv_justifications_owl:ObjectivesImpaired
is_a: NonFulfilmentJustification
class_uri: justifications:ObjectivesImpaired

```
</details>

### Induced

<details>
```yaml
name: ObjectivesImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ObjectivesImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it impairs the objectives of associated context'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Objectives Impaired
exact_mappings:
- dpv_justifications:ObjectivesImpaired
- dpv_justifications_owl:ObjectivesImpaired
is_a: NonFulfilmentJustification
class_uri: justifications:ObjectivesImpaired

```
</details></div>