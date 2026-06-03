---
search:
  boost: 10.0
---

# Class: Deployer 


_Actor that deploys Technology_



<div data-search-exclude markdown="1">



URI: [tech:Deployer](https://w3id.org/lmodel/dpv/tech/Deployer)





```mermaid
 classDiagram
    class Deployer
    click Deployer href "../Deployer/"
      Actor <|-- Deployer
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Deployer**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Deployer](https://w3id.org/lmodel/dpv/tech/Deployer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Deployer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | AI Act |
| upstream_iri | https://w3id.org/dpv/tech/owl#Deployer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Deployer |
| native | tech:Deployer |
| exact | dpv_tech:Deployer, dpv_tech_owl:Deployer |
| close | iso22989:Stakeholder |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Deployer
annotations:
  dct_source:
    tag: dct_source
    value: AI Act
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Deployer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that deploys Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Deployer
exact_mappings:
- dpv_tech:Deployer
- dpv_tech_owl:Deployer
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Deployer

```
</details>

### Induced

<details>
```yaml
name: Deployer
annotations:
  dct_source:
    tag: dct_source
    value: AI Act
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Deployer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that deploys Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Deployer
exact_mappings:
- dpv_tech:Deployer
- dpv_tech_owl:Deployer
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Deployer

```
</details></div>