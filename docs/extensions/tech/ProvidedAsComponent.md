---
search:
  boost: 10.0
---

# Class: ProvidedAsComponent 


_Technology provided as a component_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsComponent](https://w3id.org/lmodel/dpv/tech/ProvidedAsComponent)





```mermaid
 classDiagram
    class ProvidedAsComponent
    click ProvidedAsComponent href "../ProvidedAsComponent/"
      ProvisionMethod <|-- ProvidedAsComponent
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsComponent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsComponent](https://w3id.org/lmodel/dpv/tech/ProvidedAsComponent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as ComponentProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsComponent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsComponent |
| native | tech:ProvidedAsComponent |
| exact | dpv_tech:ProvidedAsComponent, dpv_tech_owl:ProvidedAsComponent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsComponent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsComponent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ComponentProvision
exact_mappings:
- dpv_tech:ProvidedAsComponent
- dpv_tech_owl:ProvidedAsComponent
is_a: ProvisionMethod
class_uri: tech:ProvidedAsComponent

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsComponent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsComponent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ComponentProvision
exact_mappings:
- dpv_tech:ProvidedAsComponent
- dpv_tech_owl:ProvidedAsComponent
is_a: ProvisionMethod
class_uri: tech:ProvidedAsComponent

```
</details></div>