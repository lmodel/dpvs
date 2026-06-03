---
search:
  boost: 10.0
---

# Class: Importer 


_Actor that imports the Technology within a jurisdiction_



<div data-search-exclude markdown="1">



URI: [tech:Importer](https://w3id.org/lmodel/dpv/tech/Importer)





```mermaid
 classDiagram
    class Importer
    click Importer href "../Importer/"
      Actor <|-- Importer
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Importer**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Importer](https://w3id.org/lmodel/dpv/tech/Importer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Importer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Importer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Importer |
| native | tech:Importer |
| exact | dpv_tech:Importer, dpv_tech_owl:Importer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Importer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Importer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that imports the Technology within a jurisdiction
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Importer
exact_mappings:
- dpv_tech:Importer
- dpv_tech_owl:Importer
is_a: Actor
class_uri: tech:Importer

```
</details>

### Induced

<details>
```yaml
name: Importer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Importer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that imports the Technology within a jurisdiction
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Importer
exact_mappings:
- dpv_tech:Importer
- dpv_tech_owl:Importer
is_a: Actor
class_uri: tech:Importer

```
</details></div>