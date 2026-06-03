---
search:
  boost: 10.0
---

# Class: Designer 


_Actor that designs Technology_



<div data-search-exclude markdown="1">



URI: [tech:Designer](https://w3id.org/lmodel/dpv/tech/Designer)





```mermaid
 classDiagram
    class Designer
    click Designer href "../Designer/"
      Actor <|-- Designer
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Designer**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Designer](https://w3id.org/lmodel/dpv/tech/Designer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Designer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | DGA 26.3 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Designer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Designer |
| native | tech:Designer |
| exact | dpv_tech:Designer, dpv_tech_owl:Designer |
| close | iso22989:Stakeholder |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Designer
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Designer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that designs Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Designer
exact_mappings:
- dpv_tech:Designer
- dpv_tech_owl:Designer
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Designer

```
</details>

### Induced

<details>
```yaml
name: Designer
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Designer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that designs Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Designer
exact_mappings:
- dpv_tech:Designer
- dpv_tech_owl:Designer
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Designer

```
</details></div>